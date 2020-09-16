#여행 가자
#https://www.acmicpc.net/problem/1976
import sys
sys.stdin = open("input.txt","r")
n=int(input()) #도시 수
m=int(input()) #여행계획에 속한 도시 수
board=[list(map(int,input().split())) for _ in range(n)]
plan=list(map(int,input().split())) #여행 계획
parent=[0]*(n+1)

for i in range(1,n+1): #부모 초기화
    parent[i]=i
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

for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            union_parent(parent,i+1,j+1)
for i in range(m-1):
    if find_parent(parent,plan[i])!=find_parent(parent,plan[i+1]):
        print("NO")
        break
else:
    print("YES")
