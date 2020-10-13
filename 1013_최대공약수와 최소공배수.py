def solution(n, m):
    answer = []
    a,b=n,m
    while n!=0:
        n,m=m%n,n
    answer.append(m) 
    answer.append(a*b//m)
    return answer
