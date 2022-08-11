def solution(arr1, arr2):
    answer = []
    for i in range(0, len(arr1)):
        inner = []
        for j in range(0, len(arr2[0])):
            sum = 0
            # j가 정답 안
            # i가 정답배열 길이
            for k in range(0, len(arr2)):
                multi = (arr1[i][k] * arr2[k][j])
                sum += multi
            inner.append(sum)
        answer.append(inner)
    return answer
