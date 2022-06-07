def solution(arr1, arr2):
    answer = [] 
    for row in range(len(arr1)):
        next_arr = []
        for col in range(len(arr1[0])):
            next_arr.append(arr1[row][col]+arr2[row][col])
        answer.append(next_arr)
    return answer