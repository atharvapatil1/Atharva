#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getCodeAtTime' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING initialCode
#  2. LONG_INTEGER minutesElapsed
#

def getCodeAtTime(initialCode, minutesElapsed):
    # Write your code here
    code = list(initialCode)
    
    for minute in range(minutesElapsed):
        # Find the best single swap that maximizes the string lexicographically
        best_i, best_j = -1, -1
        
        # For lexicographically maximum, we want to put the largest digit as early as possible
        # Try to find the leftmost position where we can put a '1' if there's a '0'
        # or find any beneficial swap
        
        found_improvement = False
        
        # Check each position from left to right
        for i in range(len(code)):
            # If current position has '0', look for '1' to the right to swap
            if code[i] == '0':
                # Find the rightmost '1' to swap with this '0'
                for j in range(len(code) - 1, i, -1):
                    if code[j] == '1':
                        best_i, best_j = i, j
                        found_improvement = True
                        break
                if found_improvement:
                    break
        
        # If we found an improvement, make the swap
        if found_improvement:
            code[best_i], code[best_j] = code[best_j], code[best_i]
        else:
            # No beneficial swap found, we've reached the maximum
            break
    
    return ''.join(code)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    initialCode = input()
    
    minutesElapsed = int(input().strip())
    
    result = getCodeAtTime(initialCode, minutesElapsed)
    
    fptr.write(result + '\n')
    
    fptr.close()