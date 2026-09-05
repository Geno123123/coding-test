"""
문제: 코니와브라운(Level 2)
링크: x Line인턴채용 코딩테스트
분류: StackQueue
"""

import heapq

def solution(scoville, K):
    shake=0
    heapq.heapify(scoville) #힙 구조로 만들기
    while(len(scoville)>1):
        n1=heapq.heappop(scoville) #최솟값 빼기1
        n2=heapq.heappop(scoville) #최솟값 빼기2
        if n1>=K:
            return shake
        shake+=1
        heapq.heappush(scoville,n1+n2*2)
    if scoville[0]>=K:
        return shake
    return -1