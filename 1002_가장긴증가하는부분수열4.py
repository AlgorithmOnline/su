#가장 긴 증가하는 부분 수열 4
#https://www.acmicpc.net/problem/14002
import sys
input=sys.stdin.readline
n=int(input())
arr=list(map(int,input().split()))
dp=[1]*(n+1)

for i in range(1,n):
    for j in range(i):
        if arr[i]>arr[j]:
            dp[i]=max(dp[i],dp[j]+1)
maxlen=max(dp)
print(maxlen)
lis=[]
for i in range(n-1,-1,-1):
    if dp[i]==maxlen: #최대길이인 것 구하기
        lis.append(arr[i])
        maxlen-=1
print(' '.join(map(str,reversed(lis)))) #lis뒤집음
