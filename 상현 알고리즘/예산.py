def solution(d, budget):
    count = 0 
    d.sort()
    for item in d:
        if budget >= item:
            budget -= item
            count +=1 
    return count