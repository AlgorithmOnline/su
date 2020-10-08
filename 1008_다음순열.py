#다음 순열
#https://www.acmicpc.net/problem/10972
import sys
sys.stdin = open("input.txt","r")
input=sys.stdin.readline
n = int(input())
a = list(map(int,input().split()))
def next_permutation(a):
    i=-1
    for index in range(len(a)-1):
        if a[index]<a[index+1]:
            i=index
    if i==-1: 
        return -1 
    for index in range(i+1,len(a)):
        if a[index]>a[i]:
            j=index
    a[i],a[j]=a[j],a[i]
    a=(a[:i+1]+sorted(a[i+1:]))
    return a

res=next_permutation(a)
if res!=-1: 
    print(' '.join(map(str,res)))
else: 
    print(-1)
