#수들의 합
#https://www.acmicpc.net/problem/1789
import sys
sys.stdin = open("input.txt","r")
n=int(input())
x=1
while(x*(x+1)/2 <=n):
    x+=1
print(x-1)
