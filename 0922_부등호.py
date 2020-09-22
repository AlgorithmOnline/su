#부등호
#https://www.acmicpc.net/problem/2529
import sys
sys.stdin = open("input.txt","r")
n=int(input())
op=input().split() 
num=[False]*10
maxv,minv="",""

def check(i,j,op):
    if op=='<':
        return i<j
    if op=='>':
        return i>j
    return True

def dfs(cnt,s):
    global maxv,minv
    if cnt==n+1:
        if not len(minv): 
            minv=s
        else:
            maxv=s
    else:
        for i in range(10):
            if num[i] == False: 
                if cnt==0 or check(s[-1],str(i),op[cnt-1]):
                    num[i]=True
                    dfs(cnt+1,s+str(i))
                    num[i]=False

dfs(0,"")
print("%s\n%s" %(maxv,minv))
