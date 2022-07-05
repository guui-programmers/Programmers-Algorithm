def solution(sizes):
    max_value = -1
    min_big_list = []
    for size in sizes:
        min_big_list.append(min(size))
        for s in size:
            if s > max_value:
                max_value = s
    max_another = sorted(min_big_list).pop()
    return max_value * max_another
