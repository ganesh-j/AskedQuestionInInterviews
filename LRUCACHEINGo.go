//Detect race condition in go
//One can find race condition if present any
//one can use -race option during build, run etc.

//Ques: asked in truecaller
//Part 1:
//Build an LRU Cache of capacity n that stores key-value objects (strings for simplicity)
//It should do the following:
//	1. Initialize an LRUCache with a capacity of n.
//    2. Get(key): Get the value of the key (string) if the key exists in the cache, otherwise return -1. Each element has a distinct key.
//	3. Put(key, value): Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item...
//... before inserting a new element.

//n = 3
//1 -> 2 -> 3

//case1: element is not present and LRU cache is not full
//   add(ele)
//	 o(1)

//	 1 -> 2
//	 100  200

//	 1 100
//	 2 200
//case2: element is already present and LRU cache is not full
//     if it is not last ele
//	     remove it and add to the last

//get add of key -> o(1) use hashmap
//then remove it and add into last
//hash

//case3: element is not present and cache is full
//remove first element from the cache
//update it into cache

//case4: element is already present and LRU cache is also full
//	   if it is not last ele
//		 same as cache 2

//		1 -> 2 -> 3

//Part 2
//You also need to implement a cleaner routine that runs concurrently in the background and cleans every key-value pair that hasn't been used for more than 10 seconds

//Below code is having part1 and part2, not sure part2 is correct or not
package main

import (
	"fmt"
	"strconv"
	"sync"
	"time"
)

type CacheNode struct {
	key            string
	value          string
	prev           *CacheNode
	next           *CacheNode
	lastUpdateTime time.Time
}

type CacheEndNode struct {
	root *CacheNode
	tail *CacheNode
}

var cacheMap = map[string]*CacheNode{}

var currentCount = 0

//var maxCount = 2
var maxCount = 10

func main() {

	cache := &CacheEndNode{
		root: nil,
		tail: nil,
	}

	var wg sync.WaitGroup
	wg.Add(1)
	go func() {
		for now := range time.Tick(10 * time.Second) {
			fmt.Println("letsee how many times tick is getting called")
			temp := cache.root
			res := []*CacheNode{}
			for temp != nil {
				elapsed := now.Sub(temp.lastUpdateTime)
				if elapsed > 10 {
					res = append(res, temp)
				}
				temp = temp.next
			}

			//remove the node one by one
			for index := 0; index < len(res); index++ {
				fmt.Println("Node to be deleted is", res[index])
				cache.remove(res[index])
			}
		}
	}()

	for i := 0; i <= 5; i++ {
		cache.Put(strconv.Itoa(i), strconv.Itoa(i))
	}

	cache.print()

	//cache.Put("foo", "bar")
	//cache.Put("john", "doe")
	//fmt.Println(cache.Get("foo")) // bar

	//cache.Put("test", "123")
	//fmt.Println(cache.Get("john")) // -1

	//cache.Put("city", "Blore")
	//fmt.Println(cache.Get("foo")) // -1

	time.Sleep(60 * time.Second)
	fmt.Println("we are printing the below list")
	cache.Put("11", "11")
	//print the list
	cache.print()
	wg.Wait()
}

func (node *CacheEndNode) print() {
	temp := node.root
	for temp != nil {
		fmt.Println("value is", temp.key)
		temp = temp.next
	}
}

func (node *CacheEndNode) Put(key, value string) {

	//if it is present
	_, isPresent := cacheMap[key]
	if !isPresent {

		newCacheNode := &CacheNode{
			key:            key,
			value:          value,
			prev:           nil,
			next:           nil,
			lastUpdateTime: time.Now(),
		}

		if currentCount != maxCount {
			//max count not reached
			node.insertAtEnd(newCacheNode)
		} else {
			//remove the head Node
			node.removeHead()
			currentCount--
			node.insertAtEnd(newCacheNode)
		}
		currentCount++

	} else {
		keyNode := cacheMap[key]
		node.remove(keyNode)
		node.insertAtEnd(keyNode)
		currentCount++
	}

}

func (endNode *CacheEndNode) insertAtEnd(nodeToBeInserted *CacheNode) {

	if endNode.root == nil {
		endNode.root = nodeToBeInserted
		endNode.tail = nodeToBeInserted
	} else {
		nodeToBeInserted.lastUpdateTime = time.Now()
		endNode.tail.next = nodeToBeInserted
		nodeToBeInserted.prev = endNode.tail
		endNode.tail = nodeToBeInserted
	}
	cacheMap[nodeToBeInserted.key] = nodeToBeInserted
}

func (endNode *CacheEndNode) removeHead() {
	if endNode.root == nil && endNode.tail == nil {
		return
	}

	temp := endNode.root
	delete(cacheMap, temp.key)
	endNode.root = temp.next
	if endNode.root != nil {
		endNode.root.prev = nil
	}
	temp = nil
}

func (endnode *CacheEndNode) remove(nodeToBeRemoved *CacheNode) {

	if nodeToBeRemoved == endnode.root {
		endnode.removeHead()
		return
	}
	//temp := nodeToBeRemoved
	if nodeToBeRemoved.prev != nil {
		nodeToBeRemoved.prev.next = nodeToBeRemoved.next
	}
	if nodeToBeRemoved.next != nil {
		nodeToBeRemoved.next.prev = nodeToBeRemoved.prev
	}
	delete(cacheMap, nodeToBeRemoved.key)
	nodeToBeRemoved.prev = nil
	nodeToBeRemoved.next = nil

	currentCount--

}

func (node *CacheEndNode) Get(key string) string {

	//temp, isPresent := cacheMap[key]
	temp, isPresent := cacheMap[key]

	if isPresent {
		//update this node
		temp.lastUpdateTime = time.Now()
		if temp == node.root {
			//if it is head node
			next := temp.next
			next.prev = nil
			node.root = next
		} else {
			//if it is not head node
			next := temp.next
			if temp.prev != nil {
				temp.prev.next = next
			}
			next.prev = temp.prev
			temp.prev = nil
			temp.next = nil
		}

		//add this into end

		node.tail.next = temp
		temp.prev = node.tail
		temp.next = nil
		node.tail = temp

		//update it into hashmap
		cacheMap[key] = temp
		return temp.value

	}

	return "-1"

}
