"""
문제: 타겟넘버 (Level 2)
링크: https://school.programmers.co.kr/learn/courses/30/lessons/43165
분류: DFS_BFS
"""

def solution(array, target):
    res_array=[]
    res_array.append(-array[0]+array[1])
    res_array.append(array[0]-array[1])
    res_array.append(-array[0]-array[1])
    res_array.append(array[0]+array[1])
    #print(res_array)

    for i in range(len(array)-2):
        for k in range(len(res_array)):
            res_array[k]+=array[i+2]
        for j in range(len(res_array)):
            res_array.append(res_array[j]-2*array[i+2])

    #print(res_array)
    count=0
    for i in res_array:
        if target==i:
            count+=1

    return count