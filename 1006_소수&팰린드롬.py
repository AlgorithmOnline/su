#소수&팰린드롬
#https://www.acmicpc.net/problem/1747
import sys
import math
sys.stdin = open("input.txt","r")
n=int(input())
maxv=1000000 + 1
sosu=[True]*(maxv)
sosu[0],sosu[1]=False,False
for i in range(2,int(math.sqrt(maxv))+1):
    j=2
    if sosu[i]==True:
        while i*j<maxv:
            sosu[i*j]=False
            j+=1
res=0
for i in range(n,maxv):
    if i==1:
        continue
    if str(i) == str(i)[::-1]: 
        if sosu[i]:
            res=i
            break
if res == 0:
    res= 1003001
print(res)
