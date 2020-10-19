#경쟁적 전염
#https://www.acmicpc.net/problem/18405
import sys
from collections import deque
sys.stdin = open("input.txt","r")
input=sys.stdin.readline
n,k=map(int,input().split())
board=[list(map(int,input().split())) for i in range(n)]
virus=[]
dh=[-1,1,0,0]
dw=[0,0,-1,1]
s,x,y =map(int,input().split()) 
def bfs():
    while q:
        v,t,curh,curw=q.popleft()
        if s==t: 
            break
        for i in range(4):
            nh=curh+dh[i]
            nw=curw+dw[i]
            if 0<=nh<n and 0<=nw<n and board[nh][nw]==0: 
                board[nh][nw]=v
                q.append((v,t+1,nh,nw)) 

for i in range(n):
    for j in range(n):
        if board[i][j]>0: 
            virus.append((board[i][j],0,i,j))

q=deque(virus)
bfs()


print(board[x-1][y-1])
