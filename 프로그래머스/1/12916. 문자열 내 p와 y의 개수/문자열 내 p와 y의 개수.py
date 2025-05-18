def solution(s):
    answer = True
    p_num = 0
    y_num = 0
    
    for i in s:
        if i == 'p' or i == 'P':
            p_num += 1
        elif i == 'y' or i == 'Y':
            y_num += 1
        else:
            continue
    if p_num == y_num:
        answer = True
    elif p_num != y_num:
        answer = False
    
    return answer

#다른풀이
def solution(s):
    answer = s.lower().count('p') == s.lower().count('y')
    return answer
