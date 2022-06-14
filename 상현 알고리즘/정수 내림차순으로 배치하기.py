def solution(n):
    item = list(str(n))
    item.sort(reverse=True)
    return int("".join(item))