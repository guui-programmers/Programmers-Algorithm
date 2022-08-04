def solution(arr):
    answer = 1
    yaksu_list = [] # [[2], [2, 3], [2, 2, 2], [2, 7]]
    for a in arr:
        yaksu_list.append(getYaksu(a))
    
    yaksu_set = set()
    for yaksu in yaksu_list:
        yaksu_set.update(yaksu)
    
    yaksu_set_list = list(yaksu_set)
    yaksu_dict = dict() 
    # {2: [1, 1, 3, 1], 3: [0, 1, 0, 0], 7: [0, 0, 0, 1]}
    for same_yaksu in yaksu_set_list: # [2, 3, 7]
        count_list = []
        for yaksu in yaksu_list: # [[2], [2, 3], [2, 2, 2], [2, 7]]
            count_list.append(yaksu.count(same_yaksu))
        yaksu_dict[same_yaksu] = count_list
    
    for k, v in yaksu_dict.items(): 
        # {2: [1, 1, 3, 1], 3: [0, 1, 0, 0], 7: [0, 0, 0, 1]}
        # v에서 큰 값 제곱해주면 됨
        answer *= (k**max(v))
    
    return answer

# 약수 리턴하는 함수 >> 8 = [2*2*2]
def getYaksu(sample):
    if sample == 1:
        return [1]
    divi = 2
    arr_list = []
    while(sample >= 2):
        if sample % divi == 0:
            arr_list.append(divi)
            sample /= divi
        else:
            divi += 1
    return arr_list
