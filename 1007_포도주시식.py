#포도주 시식
#https://www.acmicpc.net/problem/2156
import sys
sys.stdin = open("input.txt","r")
n=int(input())
arr=[int(input()) for _ in range(n)]
dp=[0]*n

dp[0]=arr[0]
if n>=2:
    dp[1]=dp[0]+arr[1]
if n>=3:
    for i in range(2,n):
        dp[i]=max(dp[i-3]+arr[i-1]+arr[i],dp[i-2]+arr[i],dp[i-1])

# print(dp)
print(max(dp))
