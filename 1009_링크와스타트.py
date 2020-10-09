#링크와스타트
#https://www.acmicpc.net/problem/15661
import sys
sys.stdin = open("input.txt","r")
input=sys.stdin.readline
n=int(input())
board=[list(map(int,input().split())) for _ in range(n)]
team=[False]*n 
minv=1e9
def dfs(d,cnt):
    global minv
    if d>=n:
        return
    if cnt> int(n//2)+1:
        return
    if cnt>=1: 
        start=link=0
        for i in range(n):
            for j in range(n):
                if team[i]==True and team[j]==True:
                    start+=board[i][j]
                elif team[i]==False and team[j]==False:
                    link+=board[i][j]
        minv=min(abs(start-link),minv)
    team[d]=True
    dfs(d+1,cnt+1)
    team[d]=False
    dfs(d+1,cnt)

dfs(0,0)
print(minv)
