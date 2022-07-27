def solution(lottos, win_nums):
    answer = []
    rank_list = {2:5, 3:4, 4:3, 5:2}
    zero_count = lottos.count(0)
    same_count = 0
    for win in win_nums:
        if win in lottos:
            same_count += 1
    zero_count += same_count
    
    if zero_count >= 6:
        answer.append(1)        
    elif zero_count <= 1:
        answer.append(6)        
    else:
        for rank, val in rank_list.items():
            if zero_count == val:
                answer.append(rank)
    
    if same_count >= 6:
        answer.append(1)        
    elif same_count <= 1:
        answer.append(6)        
    else:
        for rank, val in rank_list.items():
            if same_count == val:
                answer.append(rank)
                
    return answer
