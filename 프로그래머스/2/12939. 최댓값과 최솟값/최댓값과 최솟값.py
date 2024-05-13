def solution(s):
    answer = ''
    lst = s.split( )
    num = [int(x) for x in lst]
    mn = min(num)
    mx = max(num)
    
    answer = f'{mn} {mx}'
    return answer