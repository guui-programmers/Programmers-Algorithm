def solution(s):
    data = list(s)
    data.sort(reverse=True)
    return "".join(data)