#2048
#https://www.acmicpc.net/problem/12100
import sys
sys.stdin = open("input.txt","r")
from collections import deque
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
sol , q = 0, deque()

def get(i, j):
    if board[i][j]:
        q.append(board[i][j])
        board[i][j] = 0

def merge(i, j, di, dj):
    while q:
        x = q.popleft()
        if not board[i][j]:
            board[i][j] = x
        elif board[i][j] == x:
            board[i][j] = x*2
            i, j = i+di, j+dj
        else:
            i, j = i+di, j+dj
            board[i][j] = x

def move(k):
    if k == 0:
        for j in range(n):
            for i in range(n):
                get(i, j)
            merge(0, j, 1, 0)
    elif k == 1:
        for j in range(n):
            for i in range(n-1, -1, -1):
                get(i, j)
            merge(n-1, j, -1, 0)
    elif k == 2:
        for i in range(n):
            for j in range(n):
                get(i, j)
            merge(i, 0, 0, 1)
    else:
        for i in range(n):
            for j in range(n-1, -1, -1):
                get(i, j)
            merge(i, n-1, 0, -1)

def solve(cnt):
    global board, sol
    if cnt == 5:
        for i in range(n):
            sol = max(sol, max(board[i]))
        return
    b = [x[:] for x in board]
    for k in range(4):
        move(k)
        solve(cnt+1)
        board = [x[:] for x in b]

solve(0)
print(sol)
