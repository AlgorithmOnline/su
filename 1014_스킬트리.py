def solution(skill, skill_trees):
    cnt=0
    for x in skill_trees:
        seq=list(skill)
        for i in range(len(x)):
            if x[i] in skill: 
                if seq.pop(0)!=x[i]
                    break
        else: 
            cnt+=1
        
    return cnt
