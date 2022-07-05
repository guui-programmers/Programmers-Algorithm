def solution(arr):
    answer = []
    compare = -1
    for i in range(0,len(arr)):
        if arr[i] == compare:
            continue
        else:
            compare = arr[i]
            answer.append(arr[i])
    return answer
