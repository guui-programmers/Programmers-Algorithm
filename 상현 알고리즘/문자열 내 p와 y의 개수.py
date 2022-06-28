def solution(s):
    count_p = 0
    count_y = 0
    for value in s:
        if value =='p' or value =="P":
            count_p +=1
        if value == 'y' or value == "Y":
            count_y +=1
    return count_p == count_y