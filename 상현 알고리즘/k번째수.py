def solution(array, commands):
    result = []
    for item in commands:
        temp = array[(item[0]-1):item[1]]
        temp.sort()
        result.append(temp[item[2]-1])
    return result