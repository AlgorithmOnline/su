def solution(n):
    onecnt=bin(n).count('1')
    while True:
        n+=1
        if onecnt==bin(n).count('1'):
            return n
    return answer
