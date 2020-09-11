#시험감독
#https://www.acmicpc.net/problem/13458
import sys
sys.stdin = open("input.txt","r")
n=int(input()) 
arr=list(map(int,input().split()))
main,sub=map(int,input().split())
sol=0

for x in arr:
    if x>=main:
        x-=main
        if x%sub==0:
            sol+=x//sub
        else:
            sol+=x//sub + 1
print(sol + len(arr))
