def solution(arr1, arr2):
    result = [[0]*len(arr2[0]) for i in range(len(arr1))]
    for i in range(0,len(arr1)):
        for j in range(0,len(arr2[0])):
            for k in range(0,len(arr1[0])):
                result[i][j]+=arr1[i][k]*arr2[k][j]
           
    return result
