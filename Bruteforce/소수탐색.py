"""
문제: 소수 탐색(Level 2)
링크: https://school.programmers.co.kr/learn/courses/30/lessons/42839
분류: Bruteforce
"""


from itertools import permutations
def isPrime(num):
    if num<2:
        return 0
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return 0
    return 1

def solution(numbers):
    arr=[]
    answer = set()
    for number in numbers:
        arr.append(number)
    for i in range(1,len(arr)+1):
        p=permutations(arr,i)
        for x in p:
            num=''.join(x)
            if isPrime(int(num))==1:
                answer.add(int(num))
    return len(answer)