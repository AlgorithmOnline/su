def solution(brown, yellow):
    area=brown + yellow 
    for i in range(1,area//2): 
        if area%i==0:
            h=i 
        w=area//h 
        if (h-2)*(w-2)==yellow:
            return [w,h] 
    return -1
