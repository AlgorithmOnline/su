def solution(n):
    count = [x for x in range(n, 0, -1)] 
    arr = [[0] * n for _ in range(n)]  
    dh = [1, 0, -1]  
    dw = [0, 1, -1]
    answer=[] #답

    h, w = 0, 0
    num = 1 
    dir = 0
    arr[h][w]=num
    num+=1
    while count:
        curCnt = count.pop(0) 
        for i in range(curCnt):
            nh = h + dh[dir]
            nw = w + dw[dir]
            if 0 <= nh < n and 0 <= nw < n and arr[nh][nw]==0: 
                arr[nh][nw] = num
                num += 1
                h,w=nh,nw 
        dir = (dir + 1) % 3  

    for i in range(n):
        for j in range(n):
            if arr[i][j]!=0:
                answer.append(arr[i][j])

    return answer
