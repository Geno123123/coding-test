"""
문제: 의상 (Level 2)
링크: https://school.programmers.co.kr/learn/courses/30/lessons/42578?language=python3
분류: 해시
"""

def solution(clothes):
    dict={}
    for clothe in clothes:
        kind=clothe[1]
        if kind not in dict:
            dict[kind]=1
        else:
            dict[kind]+=1    
    answer = 1
    for k,v in dict.items():
        answer*=(v+1)
        
    return answer-1