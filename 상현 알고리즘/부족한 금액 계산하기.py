def solution(price, money, count):
    total_price = 0 
    for i in range(1,count+1):
        total_price += price*i
    if total_price < money:
        return 0
    return total_price - money