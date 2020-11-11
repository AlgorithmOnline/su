def solution(s):
    stack=[]
    
    for x in s:
        if x=='(': 
            stack.append('(')
        else:
            if stack and stack[-1]=='(':
                stack.pop()
            else:
                stack.append(')')
 
    if len(stack)==0:
        return True
    else:
        return False
