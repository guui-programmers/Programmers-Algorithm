def solution(x):
    num = 0
    change_str = str(x)
    
    for item in change_str:
        num += int(item)
        
    if x%num ==0:
        return True
    else:
        return False