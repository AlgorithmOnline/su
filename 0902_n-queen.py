# N-Queen
# https://www.acmicpc.net/problem/9663
import sys
sys.stdin = open("input.txt", "r")
n = int(input())
a,b,c=[False]*n, [False]*(2*n-1), [False]*(2*n-1)#세로줄, 오른쪽 대각선 , 왼쪽 대각선
cnt=0
def dfs(d):
    global cnt
    if d == n:
        cnt += 1
        return
    else:
        for i in range(n):
            if a[i]==False and b[d+i]==False and c[d-i+n-1]==False: #인덱스의 합과 차 같음을 이용
                a[i] = b[d+i]=c[d-i+n-1]=True
                dfs(d + 1)
                a[i] = b[d+i]=c[d-i+n-1]=False

dfs(0)
print(cnt)
