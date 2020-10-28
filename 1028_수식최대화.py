import re
from itertools import permutations
def solution(expression):
    result=[]
    expression=re.split(r'(\D)',expression)
    operators=list(permutations(['*','-','+'],3))
    
    for operator in operators:
        ex=expression[:]
        for op in operator:
            while op in ex:
                index=ex.index(op)
                ex[index-1]=str(eval(ex[index-1]+op+ex[index+1]))
                del ex[index:index+2]
        result.append(abs(int(ex[0])))
    return max(result)
