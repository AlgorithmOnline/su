onecnt,zerocnt=0,0
def quadTree(h,w,size,arr):
    global onecnt,zerocnt 
    one=True 
    zero=True
    
    for i in range(h,h+size):
        for j in range(w,w+size):
            if arr[i][j]==1:
                zero=False 
            if arr[i][j]==0: 
                one=False 
        if zero==False and one==False: 
            break
    if one==True: 
        onecnt+=1 
    elif zero==True: 
        zerocnt+=1
    else: 
        quadTree(h,w,size//2,arr) 
        quadTree(h,w+size//2,size//2,arr) 
        quadTree(h+size//2,w,size//2,arr) 
        quadTree(h+size//2,w+size//2,size//2,arr) 
        
def solution(arr):
    result=[]
    
    quadTree(0,0,len(arr),arr)
    result.append(zerocnt)
    result.append(onecnt)
    return result
