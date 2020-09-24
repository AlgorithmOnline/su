#최단경로
#https://www.acmicpc.net/problem/1753
import sys
import heapq
sys.stdin = open("input.txt","r")
input=sys.stdin.readline
v,e=map(int,input().split()) #정점의 개수, 간선의 개수
start=int(input())
graph = [[] for _ in range(v+1)]
visited = [False]*(v+1)
INF=1e9
dist=[INF]*(v+1)
for _ in range(e):
    a,b,c=map(int,input().split())
    graph[a].append((b,c)) #a에서 b로 가는 가중치 c

def dijkstra(start):
    dist[start]=0
    visited[start]=True
    q=[]
    heapq.heappush(q,(0,start))
    while q:
        c,now= heapq.heappop(q) #가장 작은 노드의 비용과 노드번호
        if dist[now]<c: #이미 처리된 적이 있는 노드면
            continue
        for i in graph[now]:
            cost=dist[now]+i[1]
            if dist[i[0]]>cost: #새로운 cost가 기존 거리보다 작다면
                dist[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)

for i in range(1,v+1):
    if dist[i]==INF:
        print("INF") 
    else:
        print(dist[i])
