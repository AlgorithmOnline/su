def solution(s):
    n=[]
    n=list(map(int,s.split(" ")))
   
    return str(min(n))+" "+str(max(n))
