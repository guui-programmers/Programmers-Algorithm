def solution(n):
    result = []
    for value in range(n,0,-1):
        if n%value == 0:
            result.append(value)
    return sum(result)