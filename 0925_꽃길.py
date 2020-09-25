#꽃길
#https://www.acmicpc.net/problem/14620
import sys
n=int(input())
board=[list(map(int,input().split())) for _ in range(n)] 
visited=[[False]*n for _ in range(n)] 
dh=[-1,1,0,0]
dw=[0,0,-1,1]
sol=1e9

def check(i,j):
    if visited[i][j]==True:
        return False
    else:
        for k in range(4):
            if visited[i+dh[k]][j+dw[k]]:
                return False
    return True

def dfs(cnt,sum):
    global sol
    if cnt==3:
        sol=min(sol,sum)
    else:
        for i in range(1,n-1): 
            for j in range(1,n-1):
                if check(i,j): 
                    visited[i][j]=False
                    cost=board[i][j]
                    for k in range(4):
                        visited[i+dh[k]][j+dw[k]]=True 
                        cost+=board[i+dh[k]][j+dw[k]]
                    dfs(cnt+1,sum+cost)
                    visited[i][j] = False
                    for k in range(4):
                        visited[i + dh[k]][j + dw[k]] = False


dfs(0,0)
print(sol)
