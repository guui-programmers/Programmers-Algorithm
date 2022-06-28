def solution(s):
    answer = ''
    up = [i for i in s if i.isupper()]
    lo = [i for i in s if i.islower()]
    
    lo.sort(reverse = True)
    up.sort(reverse = True)
    
    lo = lo + up
    return ''.join(lo)
