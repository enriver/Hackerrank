# Prim

import sys
import heapq

INF=10**8

def prims(n, edges, start_node):
    adj=dict()
    que=list()

    for start,end,weight in edges:
        if start-1 not in adj.keys():
            adj[start-1]=list()
        if end-1 not in adj.keys():
            adj[end-1]=list()

        adj[start-1].append([end-1,weight])
        adj[end-1].append([start-1,weight])
        heapq.heappush(que,[INF,start-1])
        heapq.heappush(que,[INF,end-1])

    distance=[INF]*n
    distance[start_node-1]=0
    visit=[False]*n

    heapq.heappush(que,[0,start_node-1])

    while(len(que)>0):
        weight,start=heapq.heappop(que)
        if not visit[start]:
            visit[start]=True

            for end,w in adj[start]:
                if not visit[end] and distance[end]>w:
                    distance[end]=w
                    heapq.heappush(que,[w,end])

    return sum(distance)

if __name__=="__main__":
    n,m=map(int,sys.stdin.readline().split())

    edges=list()

    for _ in range(m):
        edges.append(list(map(int, sys.stdin.readline().split())))

    start_node=int(sys.stdin.readline())

    result=prims(n,edges,start_node)

    print(result)