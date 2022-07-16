def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        yaksu = yaksuCount(i)
        if yaksu % 2 == 0:
            answer += i
            continue
        answer -= i
    return answer

def yaksuCount(number):
    answer = 0
    yaksu = number
    while(yaksu > 0):
        if number % yaksu == 0:
            answer += 1
        yaksu -= 1
    return answer
