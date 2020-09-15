#최종순위
#https://www.acmicpc.net/problem/3665
import sys
from collections import deque
sys.stdin = open("input.txt","r")

for t in range(int(input())): 
    n=int(input()) 
    indegree=[0]*(n+1)
    graph=[[False]*(n+1) for _ in range(n+1)]
    rank=list(map(int,input().split()))


    for i in range(n):
        for j in range(i+1,n):
            graph[rank[i]][rank[j]]=True
            indegree[rank[j]]+=1

    m=int(input())#바뀌는 순위
    for i in range(m):
        a,b=map(int,input().split())
        #간선방향 반대로
        if graph[a][b]:
            graph[a][b]=False
            graph[b][a]=True
            indegree[a]+=1
            indegree[b]-=1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1

    cycle=False 
    flag=True
    result=[]
    q=deque()

    for i in range(1,n+1):
        if indegree[i]==0:
            q.append(i)

    for i in range(n): 
        if len(q)==0:
            cycle=True
            break
        if len(q)>=2: #위상정렬 여러개
            flag=False
            break
        cur = q.popleft()
        result.append(cur)
        for i in range(1,n+1):
            if graph[cur][i]:
                indegree[i]-=1
                if indegree[i]==0:
                    q.append(i)

    if cycle: 
        print("IMPOSSIBLE")
    elif not flag: 
        print("?")
    else:
        for x in result:
            print(x,end=' ')
        print()
