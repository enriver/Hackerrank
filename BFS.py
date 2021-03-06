# Breadth First Search : Shortest Reach

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

# Complete the bfs function below.
def bfs(n, m, edges, s):
    graphs=[[0 for _ in range(n+1)] for _ in range(n+1)]

    for i in range(m):
        graphs[edges[i][0]][edges[i][1]]=1
        graphs[edges[i][1]][edges[i][0]]=1

    visit=set()
    visit.add(s)

    dist=[0 for _ in range(n+1)]

    que=deque()
    que.append(s)

    while que:
        pos=que.pop()

        for i in range(1, n+1):
            if graphs[pos][i]==1 and i not in visit:
                visit.add(i)

                if dist[i]==0:
                    dist[i]=dist[pos]+6
                else:
                    dist[i]=min(dist[i],dist[pos]+1)

                que.append((i))

    del dist[s]

    for i in range(len(dist)):
        if dist[i]==0:
            dist[i]=-1

    return dist[1:]
               
if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input())

        result=bfs(n, m, edges, s)
        #print(result)
        print(' '.join(map(str,result)))