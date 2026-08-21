"""
문제: 방금 그 곡 (Level 1)
링크: https://school.programmers.co.kr/learn/courses/30/lessons/17683
분류: Stack
"""


m = "ABCDEFG"
musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
# "HELLO" 가 출력되어야 합니다.

def solution(m, musicinfos):
    start=[]
    end=[]
    name=[]
    seq=[]
    dict={}
    M=[]
    for s in musicinfos:
        R=s.split(",")
        start.append(R[0])
        end.append(R[1])
        name.append(R[2])
        seq.append(R[3])
    for s in m:
        if s=='#':
            if M[-1]=='A':
                M[-1]='a'
            elif M[-1]=='C':
                M[-1]='c'
            elif M[-1]=='D':
                M[-1]='d'
            elif M[-1]=='F':
                M[-1]='f'
            elif M[-1]=='G':
                M[-1]='g'
            
        else:
            M.append(s)
    m=''.join(M) #문자열 만들기
    print(m)
    for i in range(len(musicinfos)):
        K1 = end[i].split(":")
        K2 = start[i].split(":")
        term = (int(K1[0])*60 + int(K1[1])) - (int(K2[0])*60 + int(K2[1]))
        music_Str=[]
        cnt=0
        while(len(music_Str)!=term):
            if seq[i][cnt]=='#':
                if music_Str[-1]=='A':
                    music_Str[-1]='a'
                elif music_Str[-1]=='C':
                    music_Str[-1]='c'
                elif music_Str[-1]=='D':
                    music_Str[-1]='d'
                elif music_Str[-1]=='F':
                    music_Str[-1]='f'
                elif music_Str[-1]=='G':
                    music_Str[-1]='g'
            else:
                music_Str.append(seq[i][cnt])
                cnt=(cnt+1)%len(seq[i])
        music_Str=''.join(music_Str)
        if m in music_Str:
            dict[name[i]]=term
    
    if dict:
        return max(dict, key=dict.get)

    else:
        return "None"
        
    

print(solution("ABCDEFG",["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))