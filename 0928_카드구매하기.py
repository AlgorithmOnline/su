#카드 구매하기
#https://www.acmicpc.net/problem/11052
import sys
sys.stdin = open("input.txt","r")
n=int(input())
p=[0]+list(map(int,input().split())) 
dp=[0]*(n+1) 
dp[0]=0
dp[1]=p[1]
for i in range(2,n+1):
    for j in range(1,i+1): #1~i
        dp[i]=max(dp[i],dp[i-j]+p[j])
print(dp[n])
