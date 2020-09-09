from bisect import bisect_left,bisect_right #정렬된배열에서 특정 원소를 찾을 때

#값이 [left_value,right_value] 인 데이터의 개수를 반환하는 함수 
def count_by_range(a,left_value,right_value): 
    right_index = bisect_right(a,right_value)
    left_index = bisect_left(a,left_value)
    return right_index-left_index

arr = [[] for _ in range(10001)]
reversed_arr = [[] for _ in range(10001)]

def solution(words, queries):
    answer = []
    for word in words: 
        arr[len(word)].append(word)
        reversed_arr[len(word)].append(word[::-1]) #뒤집어서 삽입
        
    for i in range(10001): #정렬
        arr[i].sort()
        reversed_arr[i].sort()
    
    for q in queries:
        if q[0] != '?': #접두사에 와일드 카드 
            res=count_by_range(arr[len(q)],q.replace('?','a'),q.replace('?','z'))
        else:
            res=count_by_range(reversed_arr[len(q)],q[::-1].replace('?','a'),q[::-1].replace('?','z'))
        answer.append(res)
    return answer
