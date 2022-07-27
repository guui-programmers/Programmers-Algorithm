def solution(nums):
    choice = len(nums)/2
    if choice <= len(set(nums)):
        return choice
    else:
        return len(set(nums))

