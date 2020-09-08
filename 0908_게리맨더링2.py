#게리맨더링2
#https://www.acmicpc.net/problem/17779
import sys
sys.stdin = open("input.txt","r")
n=int(input())
board=[[0] * (n + 1)]+[[0]+list(map(int,input().split())) for _ in range(n)]
total=0
res=1e9

def solve(x,y,d1,d2):
    #경계선 정하기
    tmp=[[0]*(n+1) for _ in range(n+1)]
    tmp[x][y]=5
    for i in range(1,d1+1):
        tmp[x+i][y-i]=5 #1번.(x, y), (x+1, y-1), ..., (x+d1, y-d1)
        tmp[x+d2+i][y+d2-i]=5 #4번. (x+d2, y+d2), (x+d2+1, y+d2-1), ..., (x+d2+d1, y+d2-d1)

    for i in range(1,d2+1):
        tmp[x+i][y+i]=5 #2번.(x, y), (x+1, y+1), ..., (x+d2, y+d2)
        tmp[x+d1+i][y-d1+i]=5 #3번.(x+d1, y-d1), (x+d1+1, y-d1+1), ... (x+d1+d2, y-d1+d2)

    #선거구 합 구하기
    #1번 선거구: 1 ≤ r < x+d1, 1 ≤ c ≤ y
    one=0
    for r in range(1,x+d1):
        for c in range(1,y+1):
            if tmp[r][c]==5:
                break
            one+=board[r][c]

    #2번 선거구: 1 ≤ r ≤ x+d2, y < c ≤ N
    two = 0
    for r in range(1, x + d2 + 1):
        for c in range(n,y,-1):
            if tmp[r][c] == 5:
                break
            two += board[r][c]

    #3번 선거구: x+d1 ≤ r ≤ N, 1 ≤ c < y-d1+d2
    three = 0
    for r in range(x + d1,n+1):
        for c in range(1, y-d1+d2):
            if tmp[r][c] == 5:
                break
            three += board[r][c]

    #4번 선거구: x+d2 < r ≤ N, y-d1+d2 ≤ c ≤ N
    four = 0
    for r in range(x+d2+1, n+ 1):
        for c in range(n, y-d1+d2-1,-1):
            if tmp[r][c] == 5:
                break
            four += board[r][c]

    five=total-one-two-three-four
    maxv=max(one,two,three,four,five)
    minv=min(one,two,three,four,five)
    return maxv-minv

#기준점 x,y,d1,d2 정하고 그 결과값 찾기
total = sum(map(sum, board))  # 전체 합
#d1, d2 ≥ 1, 1 ≤ x < x + d1 + d2 ≤ N, 1 ≤ y - d1 < y < y + d2 ≤ N
#  x + d1 + d2 ≤ N, 1 ≤ y - d1 < y < y + d2 ≤ N
for x in range(1,n+1):
    for y in range(1,n+1):
        for d1 in range(1,n+1):
            for d2 in range(1,n+1):
                if x+d1+d2>n:
                    continue
                if 1>y-d1:
                    continue
                if y+d2>n:
                    continue
                res=min(res,solve(x,y,d1,d2))

print(res)
