def solution(n, lost, reserve):
    result=0
    lost.sort()
    reserve.sort()
    for student in range(1, n+1):
        if student not in lost:
            result += 1
        else:
            if student in reserve:
                result += 1
                reserve.remove(student)
                lost.remove(student)

    for student in lost:
        if student-1 in reserve:
            result += 1
            reserve.remove(student-1)

        elif student+1 in reserve:
            result +=1
            reserve.remove(student+1)

    return result