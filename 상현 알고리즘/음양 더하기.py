def solution(absolutes, signs):
    result =0 
    for num in range(len(absolutes)):
        if signs[num] is True:
            result += absolutes[num]
        else:
            result -= absolutes[num]
    return result