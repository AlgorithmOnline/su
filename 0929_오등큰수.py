#오등큰수
#https://www.acmicpc.net/problem/17299
import sys
from collections import Counter
sys.stdin = open("input.txt","r")
n=int(input())
arr = list(map(int, sys.stdin.readline().split()))
cnt=Counter(arr)
arr =[[index,cnt[index]] for index in arr]
stack = []
result= [-1 for _ in range(n)]

for i in range(len(arr)): 
    while stack and arr[stack[-1]][1]<arr[i][1]:
        result[stack.pop()]=arr[i][0] 
    stack.append(i)
print(*result)
