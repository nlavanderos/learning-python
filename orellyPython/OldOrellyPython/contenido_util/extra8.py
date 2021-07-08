"""
fibonacci with memoization
"""

import sys


sys.setrecursionlimit(10000)
temp = {}

def fibonacci(n):

    if n in temp:
        return temp[n]

    if n==1:
        value = 1
    elif n==2:
        value = 1
    elif n > 2:
        value= fibonacci(n-1)+fibonacci(n-2)
    
    temp[n]=value
    return value



n=int(input('ingresa un n: '))
print(n,":",fibonacci(n))