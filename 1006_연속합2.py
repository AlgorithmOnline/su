#연속합 2
#https://www.acmicpc.net/problem/13398
import sys
sys.stdin = open("input.txt","r")
input=sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
res=-1e9
dp=[[0]*n for _ in range(2)]
for i in range(n):
    dp[0][i]=a[i]
    dp[1][i]=a[i]
for i in range(1,n):
    dp[0][i]=max(dp[0][i],dp[0][i-1]+a[i])
for i in range(n-2,-1,-1):
    dp[1][i]=max(dp[1][i],dp[1][i+1]+a[i])

res=max(dp[0])
for i in range(1,n-1):
    res=max(res,(dp[0][i-1]+dp[1][i+1]))
print(res)
