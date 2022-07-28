def solution(nums):
    monster = len(nums)/2 # 2 
    answer = len(list(set(nums))) # 3
    if answer > monster:
        return monster
    return answer