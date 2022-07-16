def solution(n):
    answer = 0
    samjin = ""
    idx = 0
    while(True):
        if n < 3 ** idx:
            break
        idx += 1
        
    idx = idx - 1
    while(idx >= 0):
        if ((3 ** idx) * 2) <= n:
            samjin += "2"
            n -= ((3 ** idx) * 2)
        elif (3 ** idx) <= n:
            samjin += "1"
            n -= (3 ** idx)
        else:
            samjin += "0"
        idx = idx - 1
                
    index = 0
    for sam in samjin:
        answer += int(sam) * (3**index)
        index += 1

    return answer






