# Strong Password

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    change=[False]*4

    for i in password:
        if i in numbers:
            change[0]=True
        if i in lower_case:
            change[1]=True
        if i in upper_case:
            change[2]=True
        if i in special_characters:
            change[3]=True

    cnt=0
    for i in change:
        if i==False:
            cnt+=1

    if n+cnt>6:
        return cnt
    else:
        return 6-n

if __name__ == '__main__':
    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    print(answer)