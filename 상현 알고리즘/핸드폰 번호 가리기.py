def solution(phone_number):
    count = len(phone_number)
    answer = '*'*(count-4) + phone_number[-4:]
    return answer