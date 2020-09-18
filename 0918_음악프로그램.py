#음악프로그램
#https://www.acmicpc.net/problem/2623
import sys
from collections import deque
sys.stdin = open("input.txt","r")
n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
indegree=[0]*(n+1)

for i in range(m):
    data=list(map(int,input().split()))
    sub=data[0]
    for j in range(1,len(data)-1):
        graph[data[j]].append(data[j+1])
        indegree[data[j+1]]+=1

#시작노드 넣기
q=deque()
for i in range(1,n+1):
    if indegree[i]==0:
        q.append(i)

cycle=False
result=[]
for i in range(n):
    if len(q)==0:
        break
    cur=q.popleft()
    result.append(cur)
    for i in graph[cur]:
        indegree[i]-=1
        if indegree[i]==0:
            q.append(i)
if cycle:
    print(0)
else:
    for x in result:
        print(x)
