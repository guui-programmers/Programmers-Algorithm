import re

def solution(s):
    answer = ""
    s = s.lower()
    
    blank = " "
    # blank 인덱스
    indices = [i.start() for i in re.finditer(blank, s)]
    
    # 앞이나 끝에 공백이 있는 경우 리스트에서 제거
    s_list = s.split(" ")
    for ss in s_list[:]:
        if ss == "":
            s_list.remove(ss)
    
    # 숫자로 시작하지 않는 경우 첫글자 대문자로
    for ss in s_list:
        if not ss[0].isdigit():
            ss = ss.replace(ss,ss.capitalize())
            answer += ss
        else:
            answer += ss
            
    # 공백 추가
    for indi in indices:
        tmp = answer[indi:]
        answer = answer[0:indi]
        answer += " "
        answer += tmp
        
    return answer
