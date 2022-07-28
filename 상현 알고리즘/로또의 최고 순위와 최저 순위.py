def solution(lottos, win_nums):
    score = {6:1, 5:2, 4:3, 3:4, 2:5,1:6, 0:6}
    zero = 0 
    count = 0
    for item in lottos :
        if item in win_nums:
            count +=1
        if item ==0 :
            zero +=1
    return (score[zero+count], score[count])