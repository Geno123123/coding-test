"""
문제: 문자 반복 출력하기 (Level 0)
링크: https://school.programmers.co.kr/learn/courses/30/lessons/120825
분류: basic
"""

def solution(my_string, n):
    answer = ''
    for i in range(len(my_string)):
        answer+=(my_string[i]*n)
    return answer

print(solution('hello',3))