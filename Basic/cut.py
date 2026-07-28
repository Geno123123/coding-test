"""
문제: 종이자르기 (Level 0)
링크: https://school.programmers.co.kr/learn/courses/30/lessons/120922
분류: basic
"""
def solution(M, N):
    #가로 자르고 세로 자르기
    cntM=0
    cntN=0
    res =M
    while M!=1:
        M-=1
        cntM+=1
    
    while N!=1:
        N-=1
        cntN+=1
    cntN*=res
    return cntM+cntN
print(solution(2,2))