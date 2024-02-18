def solution(array, commands):
    answer = []
    
    for command in commands:
        lis = array[command[0] - 1: command[1]]
        lis.sort()
        answer.append(lis[command[2] - 1])
        
    return answer