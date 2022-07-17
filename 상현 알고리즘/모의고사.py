def solution(answers):
    one = [1,2,3,4,5,1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    score = [0,0,0]
    result = []
    
    for index, value in enumerate(answers):
        if one[index%10] == value :
            score[0] +=1
        if two[index%8] == value :
            score[1] +=1
        if three[index%10] == value :
            score[2] +=1

    for i , v in enumerate(score):
        if v == max(score):
            result.append(i+1)
    return result