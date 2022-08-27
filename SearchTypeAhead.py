#Typeahead suggestions enable users to search for known and frequently searched terms. 
#As the user types in their query into the search box, our service should suggest top 3 terms starting with whatever the user has typed. 
#For example, if our database contains the following terms: cap, captain, or capital and the user has typed in ‘cap’ our system should suggest ‘cap’ ‘captain’ and ‘capital’ 


#Asked in Service-Now
#Input: 
#Insert/update -> [the, thumb, thunder, thank, think, cap, captain, capital, capacity], [3, 4, 7, 23, 10, 11, 23, 12, 2] 

#the -> insertInTrie()
#Search -> th ---> thank, think, thunder
#Search for tha --> thanks
#Search -> cap --> cap, captain, capital
#Q1: How to store the data?   -> Trie tree, but why trie tree, insert, delete search operation



#1.find all stringgs hacing search string as prefix , also add the ranks also
#2. sort the result based  on the rank
#3. return highest rank strings

#from types import new_class
#very good implementation of trie tree
#try to have value as key at each level
#each node will look like [[A, B, C, D, E, F, G, H, I, J, K, L, M...Z], endofNode, childcounts, rank]
#                               |
#     [[A, B, C, D, E, F, G, H, I, J, K, L, M...Z], endofNode, childcounts, rank], now it is telling these are B childs, whether it is last character of string and if it
# is , pls store its rank

#Time complexity insert: o(m) where m is length of input string
#Search: o(m) where m is length of input string
#findsuggestions: o(heightofTrie) if input string is present in trie
##Awesome
class Trie:
    
    def __init__(self, rank):
        self.end = False
        self.childs = {} #dictionary as key to value mapping
        self.count = 1
        self.rank = -1

class Trieres:
    def __init__(self, value, rank):
        self.value = value
        self.rank = rank

class TrieRoot:
    def __init__(self):
        self.root = Trie(0)

    def insert(self, input, rank):
        currNode = self.root
        for index in range(len(input)):
            key = input[index]
            if key not in currNode.childs:
                newNode = Trie(rank)
                currNode.childs[key] = newNode
                #currNode = newNode
            elif key in currNode.childs:
                #it means it is present in currNode
                currNode.childs[key].count += 1

            currNode = currNode.childs[key]

        #update the rank and end of character
        currNode.end = True
        currNode.rank = rank
    
    def search(self, input):
        #get all strings having input string as prefix
        
        res = []
        searchResults = []
        currNode = self.root
        isPresent = True

        for index in range(len(input)):
            key = input[index]
            if key in currNode.childs:
                currNode = currNode.childs[key]
            else:
                isPresent = False
                break

        if isPresent:
            if currNode.count >= 1:
                self.getRemainingStrings(currNode, input, res)
                if res:
                    output = sorted(res, key= lambda x: x.rank)
                    ##need to sort based on the rank and return the result.
                    ##one can use range function to print list in reverse order, right syntax: (lastele, firsele-1, -1/decrement step)
                    for index in range(len(output) - 1, -1, -1):
                        searchResults.append(output[index].value)
          
        return searchResults[:3]

    def getRemainingStrings(self, currNode, input, res):
        
        if currNode is None or currNode.end:
            resNode = Trieres(input, currNode.rank)
            res.append(resNode)
            return

        for key in currNode.childs:
            newInput = input + key
            self.getRemainingStrings(currNode.childs[key], newInput, res)

        return




obj = TrieRoot()
obj.insert("thank", 23)
obj.insert("think", 11)
obj.insert("thunder", 7)
obj.insert("the", 3)
obj.insert("thumb", 4)
obj.insert("cap", 11)
obj.insert("captain", 23)
obj.insert("capital", 12)
obj.insert("capacity", 2)
 #[the, thumb, thunder, thank, think, cap, captain, capital, capacity], [3, 4, 7, 23, 10, 11, 23, 12, 2] 

res = obj.search("th")
print("final res is", res)

res = obj.search("tha")
print("final res is", res)

res = obj.search("cap")
print("final res is", res)











            





