#암호 만들기
#https://www.acmicpc.net/problem/1759
import sys
from itertools import combinations
sys.stdin = open("input.txt","r")
n,m=map(int,input().split())
pos=[]
data=input().split()
data.sort()
selected=list(combinations(data,n))
# print(selected)
selected.sort()
for x in selected:
    con, vow = 0, 0
    for a in x:
        if a in 'aeiou':
            con+=1
        else:
            vow+=1
    if con>=1 and vow>=2: 
        print(''.join(x))
