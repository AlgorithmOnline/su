#임계경로
#https://www.acmicpc.net/problem/1948
import sys
from collections import deque
sys.stdin = open("input.txt","r")
n=int(input()) 
m=int(input()) 
graph=[[]*(n+1) for _ in range(n+1)]
back_graph=[[]*(n+1) for _ in range(n+1)]
indegree=[0]*(n+1) #진입차수
result=[0]*(n+1)
check=[0]*(n+1)
q=deque()
for _ in range(m):
    a,b,t=map(int,input().split())
    graph[a].append((b,t))
    back_graph[b].append((a,t))
    indegree[b]+=1
start,end=map(int,input().split())

q.append(start)

def topologysort():
    while q:
        cur=q.popleft()
        for i,t in graph[cur]:
            indegree[i]-=1
            result[i]=max(result[i],result[cur]+t)
            if indegree[i]==0:
                q.append(i)

    cnt=0
    q.append(end)
    while q:
        cur=q.popleft()
        for i,t in back_graph[cur]:
            if result[cur]-result[i]==t:
                cnt+=1
                if check[i]==0: 
                    q.append(i)
                    check[i]=1

    print(result[end])
    print(cnt)

topologysort()
