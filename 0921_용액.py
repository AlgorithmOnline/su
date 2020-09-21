#용액
#https://www.acmicpc.net/problem/2467
import sys
sys.stdin = open("input.txt","r")
n=int(input())
arr=list(map(int,input().split()))
minv=2e10
l=0
r=n-1
while l < r:
    sum=arr[l]+arr[r]
    if abs(sum)<abs(minv):
        minv=sum
        a=arr[l]
        b=arr[r]
    if sum<0:
        l+=1
    else:
        r-=1
print(a,b)
