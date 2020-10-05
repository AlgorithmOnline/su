#외판원 순회 2
#https://www.acmicpc.net/problem/10971
import sys
sys.stdin = open("input.txt","r")
input=sys.stdin.readline
n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
visited=[False]*n
res=1e9
def dfs(start,node,cost):
    global res,visited,arr
    if visited.count(True)==n:
        if arr[node][start]!=0:
            res=min(res,cost+arr[node][start])
    else:
        for i in range(n):
            if visited[i]==False and arr[node][i]!=0:
                visited[i]=True
                dfs(start,i,cost+arr[node][i])
                visited[i]=False

for i in range(n):
    visited[i]=True
    dfs(i,i,0)
    visited[i]=False
print(res)
