#You are given stones with heights
#same height stones can be merges to h+1
#return min number of stones after these operations
#ex: [1, 2, 1]: 2 **stones 1 + 1 merge result into stone 2 and then stone 2 can be merged to stone 2 result into 1**
#ex: [1, 1, 3, 2,2 , 3, 2]: 3, res=[2, 3, 4]
#ex: [1, 1, 5]: 2



# Online Python - IDE, Editor, Compiler, Interpreter
# not complete
# need to complete it again, not able to think correctly
def minStones():
   # stones = [1, 1, 3, 2, 2, 3, 2]
    stones = [1, 1, 2]
    queue = []
    stones.sort()
    for ele in stones:
        queue.append(ele)
        
    count = 0
    while len(stones) > 0:
        count = 1
        res = []
        for index in range(1, len(stones)):
            if stones[index] == stones[index - 1]:
                count += 1
            elif stones[index] != stones[index-1] and count > 1:
                res.append(stones[index-1])
                count = 1
 
        stones = None
        print("res value are", res)
        stones = res
        res = None
    
    print("value of stones is", stones)
    print("min len of stones are", len(stones))


print("lets call the main function")
minStones()
