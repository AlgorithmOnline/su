#빗물
#https://www.acmicpc.net/problem/14719
import sys
sys.stdin = open("input.txt","r")
h,w=map(int,input().split())
block=list(map(int,input().split()))
rain=0

for i in range(len(block)):
    topleft=max(block[:i+1])
    topright=max(block[i:])
    low=min(topleft,topright)
    rain=rain+abs(block[i]-low)
print(rain)
