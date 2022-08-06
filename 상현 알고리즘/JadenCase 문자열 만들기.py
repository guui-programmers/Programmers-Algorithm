def solution(s):
    answer = ''
    s_to_list = s.lower().split(" ")
    for item in s_to_list:
        if item =="":
            answer += " "
        elif item[0].isalpha() ==True:
            answer +=" "+item[0].upper() + item[1:]
        else:
            answer +=" "+item
    return answer.lstrip()