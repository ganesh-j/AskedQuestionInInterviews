##Asked in Meckinesy
##given all the expressions "<<<>>", tell expression is balanced or not, you can replace ">" with "<>". How many 
##times we can replace defined in maxReplacements
##{"<<>>", "<>>"}
##{2, 2}

## balanced or not
def balancedOrNot(expressions, maxReplacements):
    res = [0] * len(maxReplacements)
    index = 0
    for exp in expressions:
        stack = []
        count = 0
        for i in range(len(exp)):
            if (exp[i] == '<'):
                stack.append('<')
            elif stack and exp[i] == '>':
                stack.pop()
            else:
                count += 1
        
        if not stack and maxReplacements[index] >= count:
            res[index] = 1
        else:
            res[index] = 0
        
        index += 1
    
    return res
                