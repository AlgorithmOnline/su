def solution(s):
    answer = ''
    arr=s.split(" ")
    up=[]
    for x in arr:
        up.append(x.capitalize())

    
    return ' '.join(up)
