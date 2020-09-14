#게임 개발
#https://www.acmicpc.net/problem/1516
import sys
from collections import deque
import copy
sys.stdin = open("input.txt","r")
n=int(input())
graph=[[] for _ in range(n+1)]
indegree=[0]*(n+1)
time=[0]*(n+1)
q=deque()
for i in range(1,n+1):
    data = list(map(int,input().split()))
    time[i]=data[0]
    for pre in data[1:-1]:
        indegree[i]+=1
        graph[pre].append(i) 

def topologysort():
    result=copy.deepcopy(time)
    for i in range(1,n+1):
        if indegree[i]==0:
            q.append(i)

    while q:
        cur=q.popleft()
        for i in graph[cur]:
            indegree[i]-=1
            result[i] = max(result[i], result[cur]+time[i])
            if indegree[i]==0:
                q.append(i)

    for i in range(1,n+1):
        print(result[i], end=' ')
topologysort()
