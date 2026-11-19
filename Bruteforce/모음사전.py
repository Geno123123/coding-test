"""
문제: 모음사전(Level 2)
링크: https://school.programmers.co.kr/learn/courses/30/lessons/84512
분류: Bruteforce
"""

def solution(word):
    #단어의 길이는 A AA AAA AAAA AAAAA ->  A E I O U
    #            1  2   3   4     5
    #총 시간복잡도 5+25+125+625+3125.. 시간복잡도는 충분하다.
    answer = 0
    words=[]
    vowel=['A','E','I','O','U']
    word_S=""
    
    def dfs(word):
        if len(word)==5:
            return
        for ch in vowel:
            new_word=word+ch
            words.append(new_word)
            dfs(new_word)
            
    dfs(word_S)
    # print(words.index(word)+1)
            
    return words.index(word)+1

    