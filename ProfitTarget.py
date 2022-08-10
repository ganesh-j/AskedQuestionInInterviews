##Asked in Mekinsey
## calculate profit target in such a way that 
## given an array, we need to find all the pairs with target x
## atleast one element should differ

def stockPairs(stocksProfit, target):
    # Write your code here
    stockMap = {}
    totalPairs = 0
    for i in range(len(stocksProfit)):
        stockMap[stocksProfit[i]] = i
    
    for index in range(len(stocksProfit)):
        remainingTarget = target - stocksProfit[index]
        if isKeyPresent(stockMap, remainingTarget) and stockMap[remainingTarget] != -1 and stockMap[remainingTarget] != index:
            stockMap[stocksProfit[index]] = -1
            stockMap[remainingTarget] = -1
            totalPairs += 1
            
    return totalPairs
            
def isKeyPresent(stockMap, key):
    if key in stockMap:
        return True
    return False

