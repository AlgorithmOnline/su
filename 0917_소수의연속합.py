#소수의 연속합
#https://www.acmicpc.net/problem/1644
import sys
import math
sys.stdin = open("input.txt","r")
n=int(input())
arr=[True for _ in range(n+1)]
prime=[]

def isprime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if arr[i]==True:
            j=2
            while i*j<=n:
                arr[i*j]=False
                j+=1
isprime(n)
for i in range(2,n+1):
    if arr[i]:
        prime.append(i)

s,e=0,0
sum=0
cnt=0
for s in range(len(prime)):
    while e<len(prime) and sum<n: 
        sum+=prime[e] 
        e+=1
    if sum==n:
        cnt+=1
    sum-=prime[s]
print(cnt)
