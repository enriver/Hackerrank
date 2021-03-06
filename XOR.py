# SUM vs XOR

import math
import os
import random
import re
import sys

# Complete the sumXor function below.
def sumXor(n):
    x=0
    res=0

    while x<=n:
        if n+x==n^x:
            res+=1

        x+=1

    return res

if __name__ == '__main__':
    n = int(input().strip())

    result = sumXor(n)

    print(result)