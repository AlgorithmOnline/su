#https://www.acmicpc.net/problem/1717
import sys
sys.stdin = open("input.txt","r")
n,m=map(int,input().split()) 
parent=[]

def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b


for i in range(n+1):
    parent.append(i)

for _ in range(m):
    comm,a,b=map(int,input().split())
    if comm==0: 
        union_parent(parent,a,b)
    elif comm==1: 
        if find_parent(parent,a)==find_parent(parent,b): 
            print("YES")
        else:
            print("NO")
