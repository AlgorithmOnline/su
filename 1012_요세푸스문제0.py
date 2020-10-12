#요세푸스 문제 0
#https://www.acmicpc.net/problem/11866
import sys
from collections import deque
sys.stdin = open("input.txt","r")
n,k=map(int,input().split())
q=deque(i for i in range(1,n+1))
res=[]
while q:
    q.rotate(-(k-1))
    res.append(q.popleft())
i=1
cnt=0
print("<",end='')
for i in range(len(res)):
    if i==len(res)-1:
        print("%d>" %res[i])
    else:
        print("%d, " %res[i],end='')
