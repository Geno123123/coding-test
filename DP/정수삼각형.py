"""
문제: 정수삼각형(Level 3)
링크: https://school.programmers.co.kr/learn/courses/30/lessons/43105
분류: DP
"""

def circum(triangle, row, col, leng, memo):
    if row == leng - 1:
        return triangle[row][col]

    if (row, col) in memo:
        return memo[(row, col)]

    result = triangle[row][col] + max(circum(triangle, row+1, col, leng, memo),circum(triangle, row+1, col+1, leng, memo))
    memo[(row, col)] = result

    return result

def solution(triangle):
    memo={}
    answer=circum(triangle,0,0,len(triangle),memo)
    print(answer)
    return answer