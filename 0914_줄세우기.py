#줄 세우기
#https://www.acmicpc.net/problem/2252
import sys
from collections import deque
sys.stdin = open("input.txt","r")
n,m=map(int,input().split()) 
graph=[[] for _ in range(n+1)]
indegree=[0]*(n+1) #진입차수
q=deque()
result=[]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    indegree[b]+=1

def topologysort():
    for i in range(1,n+1):
        if indegree[i]==0:
            q.append(i)

    while q:
        cur=q.popleft() 
        result.append(cur)
        for i in graph[cur]:
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)

topologysort()
for x in result:
    print(x,end=' ')
