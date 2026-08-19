input = "abcabcabcabcdededededede"

#ab ca bc BC
#01 23 34 56


def string_compression(string):

    min_Cnt=len(string) #최솟값 저장
    for i in range(1,len(string)//2+1): #1개~반개만
        cnt_Str=1
        str1=""
        new_Str=""
        for j in range(0,len(string),i):
            if len(str1)==0:
                str1 = string[j:j+i]
            else:
                if str1==string[j:j+i]:
                    cnt_Str+=1
                else:
                    if cnt_Str==1:
                        new_Str=new_Str+str1
                        str1=string[j:j+i]
                    
                    else:
                        new_Str=new_Str+str(cnt_Str)+str1
                        str1=string[j:j+i]
                        cnt_Str=1
            
        if cnt_Str == 1:
            new_Str = new_Str + str1
        else:
            new_Str = new_Str + str(cnt_Str) + str1


        if len(new_Str)<min_Cnt:
            min_Cnt=len(new_Str)
    return min_Cnt


print(string_compression(input))  # 14 가 출력되어야 합니다!

print("정답 = 3 / 현재 풀이 값 = ", string_compression("JAAA"))
print("정답 = 9 / 현재 풀이 값 = ", string_compression("AZAAAZDWAAA"))
print("정답 = 12 / 현재 풀이 값 = ", string_compression('BBAABAAADABBBD'))