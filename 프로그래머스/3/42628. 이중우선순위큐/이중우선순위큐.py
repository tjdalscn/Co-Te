def solution(operations):
    answer = []
    queue = []
    
    for i in operations:
        i = i.split(" ")

        if i[0] == "I":
            queue.append(int(i[1]))
        elif i[0] == "D":
            if queue == []:
                pass
            elif i[1] == "1":
                queue.sort()
                max_value = max(queue)
                queue.remove(max_value)
            elif i[1] == "-1":
                queue.sort()
                min_value = min(queue)
                queue.remove(min_value)
    if not queue == []:         
        max_value = max(queue)
        min_value = min(queue)
        answer.append(max_value)
        answer.append(min_value)
    else:
        answer = [0,0]
    
    return answer