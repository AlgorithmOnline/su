#줄 세우기
#https://www.acmicpc.net/problem/2252
import sys
from collections import deque
sys.stdin = open("input.txt","r")
n,m=map(int,input().split()) #노드개수, 간선연결
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
        #진입차수가 0인것 큐에 삽입
        if indegree[i]==0:
            q.append(i)

    while q:
        cur=q.popleft() #큐에서 뺄때마다 연관된 간선 없애주기
        result.append(cur)
        #cur과 연결되어 있는 진입차수를 1씩 뺀다
        for i in graph[cur]:
            indegree[i]-=1
            if indegree[i]==0:#진입차수가 0인것 계속해서 큐에 넣기
                q.append(i)

topologysort()
for x in result:
    print(x,end=' ')
