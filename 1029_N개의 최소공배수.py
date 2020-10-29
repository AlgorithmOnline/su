def lcd(a,b): 
    x,y=a,b
    while a!=0:
        a,b=b%a,a 
    return x*y//b
    
def solution(arr):
    
    while len(arr)>=2:  
        a=arr.pop() 
        b=arr.pop()
        arr.append(lcd(a,b))
    
    return arr.pop()
