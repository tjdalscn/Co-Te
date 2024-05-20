def solution(s):
    answer = ''
    word = []
    
    s = s.split(" ")
    for i in s:
        if i.isalpha():
            i = i[0].upper() + i[1:len(i)].lower()
        else :
            i = i.lower()
        word.append(i)
    answer = " ".join(word)
            
    return answer