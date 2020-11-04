def solution(nums):
    n=len(nums)
    kind=[] 
    for k in nums:
        if k not in kind:
            kind.append(k)
    return min(n,len(kind))
