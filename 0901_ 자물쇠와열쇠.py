#열쇠 회전시키기
def rotate(arr):
    n=len(arr)
    rotated=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated[j][n-i-1] =arr[i][j]
    return rotated

def check(biglock):
    leng=len(biglock)//3
    for i in range(leng,leng*2):
        for j in range(leng,leng*2):
            if biglock[i][j]!=1: #합친 부분이 모두 1이 되어야함 
                return False
    return True
def solution(key, lock):
    n=len(lock)#자물쇠
    m=len(key)#열쇠
    #자물쇠의 크기를 기존의 3배로 변환
    biglock = [[0]*(n*3) for _ in range(n*3)]
    #새로운 자물쇠 가운데에 원래 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            biglock[i+n][j+n]=lock[i][j]
    #열쇠 움직여보기
    for rotation in range(4):
        key = rotate(key)#열쇠 회전
        for h in range(n*2):#자물쇠 
            for w in range(n*2):
             #자물쇠에 열쇠 끼워넣기
                for i in range(m): 
                    for j in range(m):
                        biglock[h+i][w+j]+=key[i][j] 
                if check(biglock)==True:
                    return True
                 #자물쇠에서 열쇠를 다시 빼기 (원상 복구)
                for i in range(m):
                    for j in range(m):
                        biglock[h+i][w+j]-=key[i][j]
        
    return False
