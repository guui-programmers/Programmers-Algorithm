def solution(s):
    num = int(len(s)/2)
    if len(s)%2==1:
        return s[num]
    return s[num-1:num+1]