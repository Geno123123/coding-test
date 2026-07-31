"""
문제: 곱하기 or 더하기 (Level 2)
링크: 
분류: basic
"""

def find_max_plus_or_multiply(array):
    result1=0
    for i in array:
        if i==0 or i==1 or result1==0:
            result1+=i
        else:
            result1*=i
    return result1


result = find_max_plus_or_multiply
print("정답 = 728 현재 풀이 값 =", result([0,3,5,6,1,2,4]))
print("정답 = 8820 현재 풀이 값 =", result([3,2,1,5,9,7,4]))
print("정답 = 270 현재 풀이 값 =", result([1,1,1,3,3,2,5]))