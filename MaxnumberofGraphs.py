## Asked in Mekinsey hackerrank
#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'drawingEdge' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#
MOD = int(1e9 + 7)
def drawingEdge(n):
    # Write your code here
    maxEdges = (n * (n-1)) // 2
    return (pow(2, maxEdges, MOD))

if __name__ == '__main__':

Or

MOD = int(1e9 + 7)
def drawingEdge(n):
    # Write your code here
    maxEdges = (n * (n-1)) // 2
    #return (pow(2, maxEdges, MOD))
    return power(2, maxEdges)

    
def power(base, exponent):
    res = 1
    while exponent > 0:
        if ((exponent & 1) != 0):
            res = (res * base) % MOD
        base = (base * base) % MOD
        exponent = exponent // 2 ## actual division