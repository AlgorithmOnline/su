#치즈
#https://www.acmicpc.net/problem/2636
import sys
from collections import deque
sys.stdin = open("input.txt","r")
n,m=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]
dh=[-1,1,0,0]
dw=[0,0,-1,1]
sol=0
cheese=0
def bfs():
    q=deque()
    visited=[[False]*m for _ in range(n)]
    q.append((0,0))
    visited[0][0]=True
    while q:
        curh,curw=q.popleft()
        for i in range(4):
            nh=curh+dh[i]
            nw=curw+dw[i]
            if nh<0 or nh>=n or nw<0 or nw>=m:
                continue
            if visited[nh][nw]==True:
                continue
            if board[nh][nw]>=1:
                board[nh][nw]+=1
            else: #공기
                q.append((nh,nw))
                visited[nh][nw]=True

def melt():
    global cheese
    cnt=0
    flag=False
    for i in range(n):
        for j in range(m):
            if board[i][j]>=2: #녹일 수 있는 치즈, 공기에 닿음
                board[i][j]=0 #녹임
                flag=True
                cnt += 1
    #모두 녹기 한시간전 치즈를 저장하기 위해
    if cnt:
        cheese=cnt
    return flag


while True:
    bfs()
    if melt()==True:
        sol+=1
    else:
        break

print(sol)
print(cheese)
