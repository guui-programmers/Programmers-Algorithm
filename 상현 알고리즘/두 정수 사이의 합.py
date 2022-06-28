def solution(a, b):
    result = min(a,b)
    temp = result  
    for item in range(abs(a-b)):
        result = result + 1
        temp += result 
    return temp