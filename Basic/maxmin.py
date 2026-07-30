"""
문제: 최댓값과 최솟값 (Level 2)
링크: https://school.programmers.co.kr/learn/courses/30/lessons/12939
분류: basic
"""

def solution(s):
    ar=list(map(int,s.split()));
    return str(min(ar))+" "+str(max(ar));

print(solution("-1 -2 -3 -4"));