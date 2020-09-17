#부분합
#https://www.acmicpc.net/problem/1806
import sys
sys.stdin = open("input.txt","r")
n,m=map(int,input().split()) #n,목표
arr=list(map(int,input().split()))

s,e=0,0
sum=0
sol=1e9
tmp=0
for s in range(n):
    while e<n and sum<m:
        sum+=arr[e]
        e+=1
    if sum>=m:
        tmp=e-s
        sol=min(sol,tmp) 
        sum-=arr[s]
if sol==1e9:
    print(0)
else:
    print(sol)
