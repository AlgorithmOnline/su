#가장 긴 바이토닉 부분 수열
#https://www.acmicpc.net/problem/11054
import sys
sys.stdin = open("input.txt","r")
input=sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
dp=[[1]*n for _ in range(3)]
rever_a=a[::-1]
for i in range(n):
    for j in range(i):
        if a[i]>a[j]:
            dp[0][i]=max(dp[0][i],dp[0][j]+1)
        if rever_a[i]>rever_a[j]:
            dp[1][i]=max(dp[1][i],dp[1][j]+1)
dp[1]=dp[1][::-1]
dp[2][0]=1
for i in range(1,n):
    if a[i-1]!=a[i]:
        dp[2][i]=dp[0][i-1]+dp[1][i]
print(max(dp[2]))
