def gcd(a,b):
    a,b=8,12
    while a!=0:
        a,b=b%a,a
    print(b)
    return b        

def solution(w,h):
    return w*h - (w+h-gcd(w,h))
