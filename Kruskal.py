# Kruskal (MST)

import sys

def kruskals(g_nodes, g_from, g_to, g_weight):
    parent={v:-1 for v in range(1,g_nodes+1)}

    def find(x):
        answer=list()
        while parent[x]>0:
            answer.append(x)
            x=parent[x]

        for i in answer:
            parent[i]=x

        return x

    def union(x,y):
        parent[x]+=parent[y]
        parent[y]=x

    graph=list()
    
    for x,y,z in zip(g_from, g_to, g_weight):
        graph.append([x,y,z])
    
    graph.sort(key=lambda x:x[2])

    sum=0
    for x,y,weight in graph:
        px=find(x)
        py=find(y)

        if px!=py:
            union(px,py)
            sum+=weight

    return sum

if __name__=="__main__":
    g_nodes, g_edges=map(int, sys.stdin.readline().split())

    g_from=[0]*g_edges
    g_to=[0]*g_edges
    g_weight=[0]*g_edges

    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i]=map(int,sys.stdin.readline().split())

    res=kruskals(g_nodes, g_from, g_to, g_weight)
    print(res)
