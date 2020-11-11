def solution(name):
    res=0 
    moveAlpha= [ min(ord(ch)-ord("A"),ord("Z")-ord(ch)+1) for ch in name]
    i=0
    while True:
        res+=moveAlpha[i]
        moveAlpha[i]=0  
        if sum(moveAlpha)==0: 
            break
        left,right=1,1
        while moveAlpha[i-left]==0:
            left+=1
        while moveAlpha[i+right]==0:
            right+=1
        if left < right:
            res+=left
            i+= -left 
        else:
            res+=right
            i+=right
    
    return res
