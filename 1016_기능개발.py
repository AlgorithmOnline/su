def solution(progresses, speeds):
    result = []
    
    while progresses: 
        cnt=0    
        progresses=[x+y for x,y in zip(progresses,speeds)] 
        
        while progresses and progresses[0]>=100: 
            progresses.pop(0) 
            speeds.pop(0) 
            cnt+=1
        
        if cnt!=0: 
            result.append(cnt)
        
    return result
