from collections import deque

def catch_me(cony_loc, brown_loc):

    list1 = {brown_loc}
    list2 = set()

    sec = 0

    while cony_loc <= 200000:

        sec += 1
        cony_loc += sec

        if len(list1) == 0:

            for x in list2:
                list1.add(x + 1)
                list1.add(x - 1)
                list1.add(x * 2)

            list2 = set()

            if cony_loc in list1:
                return sec

        else:

            for x in list1:
                list2.add(x + 1)
                list2.add(x - 1)
                list2.add(x * 2)

            list1 = set()

            if cony_loc in list2:
                return sec

    return False


# print(catch_me(c, b))  # 5가 나와야 합니다!

print("정답 = 3 / 현재 풀이 값 = ", catch_me(10,3))
print("정답 = 8 / 현재 풀이 값 = ", catch_me(51,50))
print("정답 = 28 / 현재 풀이 값 = ", catch_me(550,500))