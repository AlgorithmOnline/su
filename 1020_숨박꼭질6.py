#숨바꼭질 6
#https://www.acmicpc.net/problem/17087
import sys
sys.stdin = open("input.txt","r")
input=sys.stdin.readline
n,s=map(int,input().split())
brother=list(map(int,input().split()))
dis=[]
for i in range(n): 
    dis.append(abs(s-brother[i]))
res=dis[0]
def gcd(a,b): 
    while a>0:
        a,b=b%a,a
    return b
for i in range(1,n):
    res=gcd(res,dis[i]) 
print(res)

