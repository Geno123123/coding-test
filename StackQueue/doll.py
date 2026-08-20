"""
문제: 괄호변환 (Level 2)
링크: https://school.programmers.co.kr/learn/courses/30/lessons/60057
분류: Array
"""

from collections import deque

balanced_parentheses_string = "()))((()"


def get_correct_parentheses(balanced_parentheses_string):
    if len(balanced_parentheses_string) ==0:
        return ""
    u=""
    v=""
    return


print(get_correct_parentheses(balanced_parentheses_string))  # "()(())()"가 반환 되어야 합니다!

print("정답 = (((()))) / 현재 풀이 값 = ", get_correct_parentheses(")()()()("))
print("정답 = ()()( / 현재 풀이 값 = ", get_correct_parentheses("))()("))
print("정답 = ((((()())))) / 현재 풀이 값 = ", get_correct_parentheses(')()()()(())('))