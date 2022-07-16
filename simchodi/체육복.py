def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    for r in reserve[:]:
        if r in lost:
            del reserve[reserve.index(r)]
            del lost[lost.index(r)]
            
    for r in reserve[:]:
        if (r-1) in lost:
            del lost[lost.index(r-1)]
            del reserve[reserve.index(r)]
        elif (r+1) in lost:
            del lost[lost.index(r+1)]
            del reserve[reserve.index(r)]
            
    return n - len(lost)
