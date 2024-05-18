def solution(A,B):
    answer = 0
    mx = 0
    A = sorted(A)
    B = sorted(B,reverse=True)
    for i in range(len(A)):
        mul = A[i] * B[i]
        mx += mul

    if answer < mx:
        answer = mx
    return answer