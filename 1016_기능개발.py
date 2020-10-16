def solution(progresses, speeds):
    result = []
    
    while progresses: 
        cnt=0    
        progresses=[x+y for x,y in zip(progresses,speeds)] #93+1,30+30,55+5 
        
        while progresses and progresses[0]>=100: #현재 진행중인 기능이 100이 넘으면, 나머지 것들중 완성된 것도 같이 배포
            progresses.pop(0) #배포한 기능제거
            speeds.pop(0) #배포한 기능의 속도 제거
            cnt+=1
        
        if cnt!=0: #배포된 것이 1개이상이면 
            result.append(cnt)
        
    return result
