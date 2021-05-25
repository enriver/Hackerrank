# Largest Permutation

import sys

'''
TimeOut

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
'''
def largestPermutation(K,ARR):
    index=[0 for _ in range(n+1)]
    for i in range(n):
        index[ARR[i]]=i
    
    for i in range(n):
        if K==0:
            break

        if i!=index[n-i]: # 현재 인덱스가 최대값의 인덱스인지 확인
            temp=ARR[i]
            ARR[i]=n-i
            ARR[index[n-i]]=temp

            index[temp]=index[n-i]
            index[n-i]=i

            K-=1
        else:
            continue

    return ARR

if __name__=="__main__":
    n,k=map(int,sys.stdin.readline().split())
    arr=list(map(int,sys.stdin.readline().split()))

    result=largestPermutation(k,arr)

    print(' '.join(map(str,result)))