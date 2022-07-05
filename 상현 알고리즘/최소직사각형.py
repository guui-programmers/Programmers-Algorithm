def solution(sizes):
    x, y = 0,0 
    for item in sizes :
        item.sort()
        x =  max(x,item[0])
        y =  max(y,item[1])
    return x*y