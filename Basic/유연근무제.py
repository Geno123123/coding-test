def solution(schedules, timelogs, startday):
    n = startday
    result = 0
    cntArr = [0] * len(timelogs)

    def toMinute(t):
        return (t // 100) * 60 + (t % 100)

    for i in range(len(timelogs)):
        limit = toMinute(schedules[i]) + 10 

        for j in timelogs[i]:
            if n == 6 or n == 7: 
                n += 1
                if n == 8:
                    n = 1
                continue

            n += 1
            if toMinute(j) > limit:
                cntArr[i] = 1

        n = startday

    for i in cntArr:
        if i == 0:
            result += 1

    return result