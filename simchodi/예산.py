def solution(d, budget):
    count = 0
    answer = 0
    d.sort()
    for dd in d:
        if budget >= (count + dd):
            count += dd
            answer += 1
    return answer
