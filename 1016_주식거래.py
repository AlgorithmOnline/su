def solution(prices):
    n=len(prices)
    stack=[] 
    result=[0]*n
    for i in range(n):
        while stack and prices[stack[-1]]>prices[i]:
            top=stack.pop()
            result[top]=i-top
        stack.append(i)
    
    while stack:
        top=stack.pop()
        result[top]=n-1-top 
        
    return result
