"""
문제: 완주하지못한선수 (Level 1)
링크: https://school.programmers.co.kr/learn/courses/30/lessons/42576
분류: 해시
"""

def solution(participant, completion):
    for i in completion:
        if i in participant:
            participant.remove(i);
        
    return participant[0];        
        
print("결론: ", solution(["leo", "kiki", "eden"],["eden", "kiki"]))