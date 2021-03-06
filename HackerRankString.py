# HackerRank in a String !

import math
import os
import random
import re
import sys

# Complete the hackerrankInString function below.
def hackerrankInString(s):
    hack=list('hackerrank')

    for i in s:
        if len(hack)==0:
            return 'YES'
        if hack[0]==i:
            hack.pop(0)
            
    if len(hack)>0:
        return 'NO'
    else:
        return 'YES'

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        print(result)