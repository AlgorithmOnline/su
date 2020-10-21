from collections import deque
def solution(priorities, location):
    cnt=0 
    q=deque([(value,i) for i,value in enumerate(priorities)])
    while q:
        cur=q.popleft()
        if q and cur[0]<max(q)[0]:
            q.append(cur) 
        else:
            cnt+=1 #인쇄
            if location==cur[1]:
                break
    return cnt
