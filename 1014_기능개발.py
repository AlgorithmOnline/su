import math
def solution(progresses, speeds):
    stack=[] 
    result=[]
    
    for i in range(len(progresses)):
        cur=math.ceil((100-progresses[i])/speeds[i])
        
        if i==0:  
            stack.append(cur)
        else: 
            if stack[-1]>=cur:
                stack.append(cur)
            else:
                result.append(len(stack)) 
                stack.clear()
                stack.append(cur)
    result.append(len(stack))
    
    return result
