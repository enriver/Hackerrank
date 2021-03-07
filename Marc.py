# Marc's Cakewalk

import math
import os
import random
import re
import sys

# Complete the marcsCakewalk function below.
def marcsCakewalk(calorie):
    calorie=sorted(calorie,reverse=True)

    res=0
    for i in range(len(calorie)):
        res+=(2**i)*calorie[i]

    return res
    
if __name__ == '__main__':

    n = int(input())

    calorie = list(map(int, input().rstrip().split()))

    result = marcsCakewalk(calorie)
    print(result)


