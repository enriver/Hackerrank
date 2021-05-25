# Largest Permutation

import sys

def largestPermutation(K,ARR):
    idx=0
    while True:
        if K==0:
            break

        if idx==len(ARR):
            break

        max_idx=ARR.index(max(ARR[idx:]))

        if idx==max_idx:
            idx+=1
            continue
        else:
            max_val=ARR[max_idx]
            now_val=ARR[idx]
            temp=now_val

            ARR[idx]=max_val
            ARR[max_idx]=temp
            K-=1
            idx+=1

    return ARR

if __name__=="__main__":
    n,k=map(int,sys.stdin.readline().split())
    arr=list(map(int,sys.stdin.readline().split()))

    result=largestPermutation(k,arr)

    print(' '.join(map(str,result)))