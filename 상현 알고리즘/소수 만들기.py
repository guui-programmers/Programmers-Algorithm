def check(n):
    count = 0 
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count == 2:
        return True
        
def solution(nums):
    result = 0
    
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):
                y = nums[i]+nums[j]+nums[k]
                print(y)
                if check(y)==True:
                    result +=1
    return result