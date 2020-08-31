#병사 배치하기
#https://www.acmicpc.net/problem/18353
import sys
sys.stdin = open("input.txt","r")

n=int(input())
arr=list(map(int,input().split()))
arr.reverse()
dp=[1]*n

#LIS
for i in range(n):
    for j in range(i):
        if arr[j]<arr[i]:
            dp[i]=max(dp[i],dp[j]+1)
print(n-max(dp))
