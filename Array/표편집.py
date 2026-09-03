"""
문제: 표 편집 (Level 3)
링크: https://school.programmers.co.kr/learn/courses/30/lessons/81303
분류: Array/List
"""
def solution(n, k, cmd):
    Z_stack = []

    prev = [i - 1 for i in range(n)]
    next = [i + 1 for i in range(n)]

    prev[0] = -1
    next[n - 1] = -1

    for c in cmd:

        if c[0] == 'D':
            x = int(c[2:])
            for _ in range(x):
                k = next[k]

        elif c[0] == 'C':
            Z_stack.append(k)

            p = prev[k]
            q = next[k]

            if p != -1:
                next[p] = q

            if q != -1:
                prev[q] = p

            if q != -1:
                k = q
            else:
                k = p

        elif c[0] == 'U':
            x = int(c[2:])
            for _ in range(x):
                k = prev[k]

        elif c[0] == 'Z':
            out = Z_stack.pop()

            p = prev[out]
            q = next[out]

            if p != -1:
                next[p] = out

            if q != -1:
                prev[q] = out

    answer = ['O'] * n

    for x in Z_stack:
        answer[x] = 'X'

    return ''.join(answer)