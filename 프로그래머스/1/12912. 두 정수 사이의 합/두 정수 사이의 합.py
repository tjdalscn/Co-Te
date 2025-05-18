def solution(a, b):
    answer = 0
    if a < b:
        for i in range(a+1, b):
            a += i 
        answer = a + b
    elif a > b:
        for i in range(b+1, a):
            b += i 
        answer = b + a
    elif a == b:
        answer = a
    return answer