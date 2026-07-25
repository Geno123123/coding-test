"""
문제: 폰켓몬 (Level 1)
링크: https://school.programmers.co.kr/learn/courses/30/lessons/1845
분류: 해시
"""

def solution(nums):
    N=len(nums)//2;
    answer = 0
    #종류 수를 출력
    nums=list(set(nums)); # 중복 삭제
    if len(nums)>=N:
        return N
    else:
        return len(nums)


print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))