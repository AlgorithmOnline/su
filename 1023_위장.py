def solution(clothes):
    cnt={} 
    result=1 
    for cloth,kind in clothes:
        if kind in cnt:
            cnt[kind]+=1
        else: 
            cnt[kind]=1
    for x in cnt.values(): 
        result*=(x+1)
    result-=1 
    return result
