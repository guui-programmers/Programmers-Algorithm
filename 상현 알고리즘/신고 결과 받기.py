from collections import defaultdict

def solution(id_list, report, k):
    result = []
    
    attack_user = defaultdict(set) # 신고 당한 사람이 key
    user = defaultdict(set)  # 신고한 사람이 key 
    
    for item in report:
        key, value = item.split(' ') 
        user[value].add(key) 
        attack_user[key].add(value) 

    for item in id_list:
        count = 0
        for j in attack_user[item]:
             if len(user[j]) >= k: 
                count += 1
        result.append(count)
        
    return result