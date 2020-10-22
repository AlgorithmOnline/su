def solution(number, k):
    stack=[]
    
    for x in number: 
        while stack and stack[-1]<x and k>0:
            stack.pop()
            k-=1 #제거
        stack.append(x)
    while k>0:
        stack.pop() 
        k-=1
    
    return ''.join(stack)
