#수들의 합 2
#https://www.acmicpc.net/problem/2003
import sys
sys.stdin = open("input.txt","r")
n,m=map(int,input().split())
arr=list(map(int,input().split()))
s,e=0,0
cnt=0
sum=0
for s in range(n):

    while sum<m and e<n:
        sum+=arr[e]
        e+=1
    if sum==m: #부분합과 같으면
        cnt+=1
    #합이 m보다 크면
    sum-=arr[s]
print(cnt)
