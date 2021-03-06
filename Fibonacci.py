# Fibonacci Modified

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the fibonacciModified function below.
def fibonacciModified(t1, t2, n):
    now=2
    
    while now<n:
        value=t1+t2**2
        t1=t2
        t2=value

        now+=1
        
    return value


if __name__ == '__main__':
    t1T2n = input().split()

    t1 = int(t1T2n[0])

    t2 = int(t1T2n[1])

    n = int(t1T2n[2])

    result = fibonacciModified(t1, t2, n)

    print(result)
