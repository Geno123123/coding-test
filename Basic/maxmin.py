def solution(s):
    ar = s.split(' ');
    arr = []
    for i in ar:
        arr.append(int(i));
    maxN = str(max(arr))
    minN = str(min(arr))
    strR=""
    strR+=minN
    strR+=" "
    strR+=maxN
    return strR


print(solution("-1 -2 -3 -4"));