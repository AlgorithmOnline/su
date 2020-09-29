#오큰수
#https://www.acmicpc.net/problem/17298
import sys
sys.stdin = open("input.txt","r")
n=int(input())
arr = list(map(int, sys.stdin.readline().split()))
stack = []
result= [-1 for _ in range(n)]

for i in range(len(arr)): 
    while stack and arr[stack[-1]]<arr[i]:
        result[stack.pop()]=arr[i]
    stack.append(i)
print(*result)
