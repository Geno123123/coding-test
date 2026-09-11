"""
문제: 체육복 (Level 1)
링크: https://school.programmers.co.kr/learn/courses/30/lessons/42862
분류: Greedy
"""

def solution(n, lost, reserve):
    lost2 = [r for r in lost if r not in reserve]
    reserve2 = [r for r in reserve if r not in lost]
    lost2.sort()
    reserve2.sort()
    for i in reserve2:
        if i - 1 in lost2:
            lost2.remove(i - 1)
        elif i + 1 in lost2:
            lost2.remove(i + 1)

    return n - len(lost2)