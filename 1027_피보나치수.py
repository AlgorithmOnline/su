def solution(n):
    memoi=[0 for i in range(n+1)]
    memoi[1]=1
    for i in range(2,n+1):
        memoi[i]=(memoi[i-1]+memoi[i-2])%1234567
    return memoi[n]
