def solution(s):
    result= []
    strings = s.split(" ")
    for item in strings:
        ch=""
        for i,value in enumerate(item):
            if i%2==0:
                ch += value.upper()
            else :
                ch += value.lower()
        result.append(ch)
    answer = " ".join(result)
    return answer