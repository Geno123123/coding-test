"""
문제: [1차]추석 트래픽 (Level 3)
링크: https://school.programmers.co.kr/learn/courses/30/lessons/17676
분류: 구현, 문자열, 슬라이딩 윈도우
"""

def solution(lines):
    start=[]
    end=[]
    for line in lines:
        arr2 = line.split(" ")[1] #시간
        arr=arr2.split(":")
        term = float(line.split(" ")[2].split("s")[0]) #텀 시간
        end.append(int(arr[0])*3600+int(arr[1])*60+float(arr[2]))
        start.append(int(arr[0])*3600+int(arr[1])*60+float(arr[2])-(term-0.001))
    maxCnt=0
    for i in range(len(start)):
        cnt=0
        for j in range(len(start)):
            if start[j] < end[i] + 1 and end[j] >= end[i]:
                cnt+=1
        if maxCnt<cnt:
            maxCnt=cnt
        # print(cnt)
    
    return maxCnt

lines = ["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]
print(solution(lines))