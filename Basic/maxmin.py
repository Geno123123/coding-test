"""
문제: 최댓값과 최솟값 (Level 2)
링크: https://school.programmers.co.kr/learn/courses/30/lessons/12939
분류: basic
"""

def solution(s):
    ar = s.split(' ');
    arr = []
    for i in ar:
        arr.append(int(i));
    maxN = str(max(arr))
    minN = str(min(arr))
    strR=""
    strR+=minN
    strR+=" "
    strR+=maxN
    return strR


print(solution("-1 -2 -3 -4"));