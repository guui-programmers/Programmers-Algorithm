def solution(nums):
    sum_list = []
    for i in range(0, len(nums) - 2):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                sum_list.append(nums[i]+nums[j]+nums[k])
                
    del_list = []
    for sosu in sum_list:
        for i in range(2, sosu):
            if sosu % i == 0:
                del_list.append(sosu)
                break
    
    for del_val in del_list:
        if del_val in sum_list:
            sum_list.remove(del_val)
            
    return len(sum_list)
