def solution(s):
    answer = []
    s = s[2:-2]
    s = s.split("},{") 
    s.sort(key = len)

    for i in s:
        tmp = i.split(',')
        for n in tmp:
            if int(n) not in answer: 
                answer.append(int(n))
    return answer
