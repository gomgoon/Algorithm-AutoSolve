from collections import deque

def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    s_lost = set(lost) - set(reserve)
    s_reserve = set(reserve) - set(lost)
    
    answer = n - len(s_lost) # 현재 참여하는 학생 수
    
    for i in s_reserve: # 여별 학생 리스트 순회
        if i - 1 in s_lost:
            answer += 1
            s_lost.remove(i-1)
        elif i + 1 in s_lost:
            answer += 1
            s_lost.remove(i+1)
    
    return answer