# Time Conversion

import os
import sys

def timeConversion(s):
    hour,minute,seconds=s.split(':')
    second, ampm=seconds[:2], seconds[-2:]

    if ampm=='PM':
        if hour=='12':
            return s[:-2]
        else:
            return str(int(hour)+12)+s[2:-2]

    else:
        if hour=='12':
            hour='00'

        return hour+s[2:-2]
        
if __name__ == '__main__':
    s = input()

    result = timeConversion(s)

    print(result)