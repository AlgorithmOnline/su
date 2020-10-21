import heapq
def solution(scoville, K):
    cnt = 0
    hq=[]
    for x in scoville:
        heapq.heappush(hq,x) 
    while hq:
        if hq[0]>=K: 
            break
        elif len(hq)==1: 
            return -1
        else:
            b=heapq.heappop(hq) 
            a=heapq.heappop(hq) 
            heapq.heappush(hq,2*a+b)
            cnt+=1
            
    return cnt
