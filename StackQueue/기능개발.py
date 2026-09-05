"""
문제: 기능개발 (Level 2)
링크: https://school.programmers.co.kr/learn/courses/30/lessons/42586
분류: Stack
"""

def solution(progresses, speeds):
    answer = []  
    dist=[]
    period=0
    for i in range(len(progresses)):
        time=0
        while progresses[i]<100:
            progresses[i]+=speeds[i]
            time+=1
        answer.append(time)
    out=0
    period=answer[0]
    for number in answer[1:]:
        if number<=period:
            out+=1
        else:
            period=number
            dist.append(out+1)
            out=0             
    dist.append(out+1)
            
    return dist

print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))
