def solution(n):
    fibo = [0,1]
    start = 0
    right = 1
    hab = 0
    for i in range(0,n-2):
        hab = start + right
        start = right
        right = hab
        fibo.append(hab)
    return (fibo[n-1] + fibo[n-2]) % 1234567


