#뱀
#https://www.acmicpc.net/problem/3190
import sys
from collections import deque
n=int(input())
board=[ [0]*(n+1) for _ in range(n+1)]
time=[]
dh=[-1,0,1,0] # 북 동 남 서
dw=[0,1,0,-1]
h,w=0,0, #뱀의 처음 위치
th,tw=0,0 #꼬리 위치
board[h][w]=2
t=0 #시간
dir = 1  # 처음 : 오른쪽으로 출발
q=deque()
q.append((h,w)) #뱀의 꼬리와 길이를 위해서 필요
k=int(input())
for _ in range(k):
    a,b=map(int,input().split())
    board[a-1][b-1]=1

l=int(input())

for i in range(l):
    c,d = input().split()
    time.append((int(c),d))
flag,direction=time.pop(0)

def turn_right(dir):#오른쪽 회전 0->1,1->2,2->3,3->0
    dir=(dir+1)%4
    return dir
def turn_left(dir): #왼쪽 회전 0->3, 3->2, 2->1, 1->0
    dir=(dir+3)%4
    return dir

while True:

    nh=h+dh[dir]
    nw=w+dw[dir]
    if nh<0 or nh>=n or nw<0 or nw>=n or board[nh][nw]==2: #벽에 부딪히면, 자기자신과 부딪히면
        t+=1
        print(t)
        break
    if board[nh][nw]==1: #사과가 있을 경우
        board[nh][nw]=2
        q.append((nh,nw)) #머리를 새롭게 넣기
    else: #사과가 없으면
        board[nh][nw]=2 #이동하고
        q.append((nh,nw)) #머리 새롭게 넣기
        #꼬리 찾기 -> 맨 처음 들어간게 꼬리
        th,tw=q.popleft()
        board[th][tw] = 0  # 꼬리 자르기
    h, w = nh, nw
    t += 1
    if t==flag: #방향전환을 할 시간이라면
        if direction=='D': #오른쪽으로 90도 방향 회전
            dir=turn_right(dir)
        else:
            dir=turn_left(dir)
        if len(time)>0:
            flag, direction = time.pop(0)
