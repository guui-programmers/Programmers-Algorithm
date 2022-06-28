def solution(strings, n):
    strings.sort()
    result = sorted(strings,key=lambda x:x[n])
    return result