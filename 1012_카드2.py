#https://www.acmicpc.net/problem/2164
import sys
from collections import deque
sys.stdin = open("input.txt","r")
n=int(input())
q=deque()
for i in range(1,n+1):
    q.append(i)

while len(q)>1:
    q.popleft()
    card=q.popleft()
    q.append(card)
print(q.pop())
