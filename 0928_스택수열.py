#스택 수열
#https://www.acmicpc.net/problem/1874
import sys
sys.stdin = open("input.txt","r")
n=int(input())
stack=[]
op=[]
cnt=1
flag=True 
for i in range(n):
    num=int(input()) 
    while cnt<=num: 
        stack.append(cnt)
        op.append('+')
        cnt+=1
    if stack[-1]==num: 
        stack.pop()
        op.append('-')
    else: 
        flag=False

if flag==True:
    print('\n'.join(op))
else: 
    print("NO")
