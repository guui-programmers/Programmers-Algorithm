def lcm(x,y):
    for num in range(max(x,y),x*y+1):
        if num%x==0 and num%y==0:
            return num 

def solution(arr):
    if len(arr)==1:
        return arr[0]
    result = lcm(arr[0],arr[1])
    for i in range(2,len(arr)):
            result = lcm(result,arr[i])
    return result