def solution(n):
    arr=['4','1','2']
    answer=""
    
    while n:
        answer=arr[n%3]+answer
        n=n//3 - (n%3==0)
    return answer
