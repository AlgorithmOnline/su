from itertools import combinations
import math
def isprime(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            return False
    return True
    
def solution(nums):
    cnt=0
    candi=[]
    selected=list(combinations(nums,3))
     
    for x,y,z in selected: 
        candi.append(x+y+z) 
    
    for x in candi:
        if isprime(x):
            cnt+=1
    
    return cnt
