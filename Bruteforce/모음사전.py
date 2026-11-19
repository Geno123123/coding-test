"""
문제: 카펫(Level 2)
링크: https://school.programmers.co.kr/learn/courses/30/lessons/42842
분류: Bruteforce
"""

def solution(brown, yellow):
    #가능한 가로와 세로의 길이?
    answer = []
    #widht>=height
    # brown+yellow=height*width
    #(width-2)*(height-2)=yellow 일 때 가로와 세로의 길이를 구해서 넣어라.
    #언제까지?
    for i in range(3, 5000):
        for j in range(3,i+1):
            if (brown+yellow)==j*i and (i-2)*(j-2)==yellow:
                answer.append(i)
                answer.append(j)
            if brown+yellow<j*i:
                break
    return answer