#트리의 부모 찾기
#https://www.acmicpc.net/problem/11725
import sys
from collections import deque
sys.stdin = open("input.txt","r")
n=int(input())
tree=[[] for _ in range(n+1)]
visited=[False]*(n+1)
res=[0]*(n+1)

for _ in range(n-1):
    a,b=map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

q=deque([1]) 
def bfs():
    while q:
        parent=q.popleft()
            if not visited[x]:
                res[x]=parent
                visited[x]=True
                q.append(x)
bfs()
print('\n'.join(map(str,res[2:])))
