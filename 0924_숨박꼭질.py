#숨박꼭질
#https://www.acmicpc.net/problem/6118
import sys
import heapq
sys.stdin = open("input.txt","r")
n,m=map(int,input().split())
graph = [[] for _ in range(n+1)]
visited=[False]*(n+1)
INF=1e9
dist=[INF]*(n+1)
for i in range(m):
    a,b=map(int,input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))

def dijstra(start):
    visited[start]=True
    dist[start]=0
    q=[]
    heapq.heappush(q,(0,1))
    while q:
        c,now = heapq.heappop(q)
        for i in graph[now]:
            cost = dist[now]+i[1]
            if dist[now]<c:
                continue
            if cost<dist[i[0]]:
                dist[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
dijstra(1)

maxv=max(dist[1:])

cnt=0
for i in range(n,0,-1):
    if maxv==dist[i]:
        index=i
        cnt+=1

print(index,maxv,cnt)
