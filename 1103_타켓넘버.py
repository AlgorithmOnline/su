cnt=0
def dfs(d,n,res,numbers,target):
    global cnt
    if d==n-1:
        if res==target:
            cnt+=1
    else:
        dfs(d+1,n,res+numbers[d+1],numbers,target) 
        dfs(d+1,n,res-numbers[d+1],numbers,target) 
        
def solution(numbers, target):
  
    dfs(-1,len(numbers),0,numbers,target)
    return cnt
