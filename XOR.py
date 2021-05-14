# SUM vs XOR
'''
https://www.snoopybox.co.kr/1863 풀이
'''

# Complete the sumXor function below.
def sumXor(n):
    if n==0:
        return 1
    else:
        return 2**(bin(n).count('0')-1)

if __name__ == '__main__':
    n = int(input().strip())

    result = sumXor(n)

    print(result)