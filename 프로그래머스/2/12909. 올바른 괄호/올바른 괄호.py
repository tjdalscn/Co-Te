def solution(s):
    answer = True
    r = 0
    l = 0
    f = []
    for i in s:
        f.append(i)
        if l > r :
            answer = False
            break
        elif i == '(':
            r += 1
        elif i == ')':
            l += 1
            
    if r != l:
        answer = False
    if f[0] == ")" or f[len(f)-1] == "(":
        answer = False
    
    return answer