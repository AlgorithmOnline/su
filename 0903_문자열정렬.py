import sys
sys.stdin = open("input.txt","r")
s=input()
leng=len(s)
alpha=[]
sum=0
for i in range(leng):
    if ord('A')<= ord(s[i]) <= ord('Z'): #s[i].isalpha() :  알파벳인지 판별하는 함수
        alpha.append(s[i])
    else:
        sum+=int(s[i])

alpha.sort()
alpha.append(str(sum))

for x in alpha: #print(''.join(alpha))
    print(x,end='')
