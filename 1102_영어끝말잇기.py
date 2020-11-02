def solution(n, words):
    turn=0
    num=1
    for i in range(1,len(words)):
        word=words[i]
        num%=n
        if words[i-1][-1]!=word[0] or word in words[0:i]: 
            turn=i//n+1
            return [num+1,turn] 
        num+=1
    return [0,0]
