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

#다른 풀이
def solution(a, b):
    if a > b:
        a, b = b, a
    answer = sum(range(a, b + 1))
    return answer
