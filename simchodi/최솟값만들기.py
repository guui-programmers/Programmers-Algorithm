def solution(A,B):
    answer = 0
    
    if (sum(A)/len(A)) > (sum(B)/len(B)):
        A.sort(reverse=True)
        B.sort()
    else:
        A.sort()
        B.sort(reverse=True)
    
    for a, b in zip(A, B):
        answer += a*b
    return answer
