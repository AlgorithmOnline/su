def solution(s):
    answer = 0

    stack=[]
    for i in range(len(s)):
        if len(stack)==0 or stack[-1]!=s[i]:
            stack.append(s[i])
        else:
            stack.pop()
    if stack:
        return 0
    else:
        return 1
