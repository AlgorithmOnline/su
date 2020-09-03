def balanced_paren(p):
    cnt=0
    for i in range(len(p)):
        if p[i]=='(':
            cnt+=1
        else:
            cnt-=1
        if cnt==0:
            return i 
        #전제가 균형잡힌 문자열을 받은 것이므로 return 이 없을 순 없음 

def paren(p):
    cnt=0
    for x in p:
        if x=='(':
            cnt+=1
        else:
            if cnt==0:
                return False
            cnt-=1
    return True

def solution(p):#p는 균형잡힌 문자열
    answer = ''
    if p=='':
        return answer
    index= balanced_paren(p)
    u=p[:index+1]
    v=p[index+1:]
    
    if paren(u):
        answer=u+solution(v)
    else: #올바른 문자열이 아니면
        answer='('
        answer+=solution(v)
        answer+=')'
        u=list(u[1:-1])
        for i in range(len(u)):
            if u[i]==')':
                u[i]='('
            else:
                u[i]=')'
        answer+="".join(u)
    return answer
