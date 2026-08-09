def solution(array, commands):
    answer = []
    for a in commands:
        i=a[0]
        j=a[1]
        k=a[2]
        arr = array[i-1:j]
        arr=sorted(arr)
        answer.append(arr[k-1])
        
    return answer