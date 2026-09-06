"""
문제: 소수 탐색(Level 2)
링크: https://school.programmers.co.kr/learn/courses/30/lessons/42839
분류: Bruteforce
"""


from itertools import permutations
def isPrime(num):
    if num==1 or num==0:
        return 0
    for i in range(2,num):
        if num%i==0:
            return 0
    return 1

def solution(numbers):
    arr=[]
    answer = []
    for number in numbers:
        arr.append(number)
    for i in range(1,len(arr)+1):
        p=permutations(arr,i)
        for x in p:
            num=''.join(x)
            # print(num)
            if isPrime(int(num))==1:
                if int(num) not in answer:
                    answer.append(int(num))
    return len(answer)