def solution(n):
    answer = ""
    item = ['수','박'] 
    for i in range(n):
        if i%2==0:
            answer+=item[0]
        else:
            answer+=item[1]
    return answer