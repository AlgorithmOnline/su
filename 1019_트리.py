#트리
#https://www.acmicpc.net/problem/1068
import sys
from collections import deque
sys.stdin = open("input.txt","r")
n=int(input()) 
tree=[[] for _ in range(n)] 
parents=list(map(int,input().split())) 
d=int(input()) 
def dfs(root): 
    global cnt
    if len(tree[root])==0: 
        cnt+=1
    else:
        for x in tree[root]:
            dfs(x)

for i in range(n):
    if parents[i]==-1:
        root=i 
    else:
        tree[parents[i]].append(i)

for i in range(n):
    if d in tree[i]:
        tree[i].remove(d)

if d!=root:
    dfs(root) 
