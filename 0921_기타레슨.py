#기타 레슨
#https://www.acmicpc.net/problem/2343
import sys
sys.stdin = open("input.txt","r")
n,m=map(int,input().split())
arr=list(map(int,input().split()))
left=max(arr)
right=sum(arr)
while left<=right:
    mid=(left+right)//2
    sum=0
    cnt=1 
    for x in arr:
        sum+=x
        if sum>mid:
            cnt+=1
            sum=x
    if cnt>m: 
        left=mid+1 
    else: 
        result = mid
        right=mid-1
print(result)
