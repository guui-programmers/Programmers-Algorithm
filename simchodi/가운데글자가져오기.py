def solution(s):
    index = int(len(s)/2)
    if(len(s) % 2 == 0):
        return(s[index-1:index+1])
    return s[index]
