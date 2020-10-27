def solution(n):
    cnt=0
    for i in range(1,n+1): # 1~n까지 차례대로 기준 설정 
        sum=0
        for j in range(i,n+1): #기준점부터
            sum+=j
            if sum==n: #합이 n과 같으면 
                cnt+=1
                break
            elif sum>n: #합이 n보다 크면 더 할 필요없음 
                break
    return cnt
