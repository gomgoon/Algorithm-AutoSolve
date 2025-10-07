def solution(friends, gifts):
    # friends = 이름
    # gifts = 전달
    # 출력값 = 다음달 가장 많이받는 친구의 선물 수
    
    gives = []
    answer = []
    length = len(friends)
    give_points = []
    
    for gift in gifts:
        gives.append(gift.split())
    
    for friend in friends:
        give_point = 0
        for give in gives:
            if give[0] == friend: # 주는 사람일 때
                give_point += 1 # 선물지수 상승
            
            if give[1] == friend: # 받느 사람일때
                give_point -= 1 # 선물지수 하락
        give_points.append(give_point)
    
    for idx, friend in enumerate(friends):
        arr = [0] * length
        num = 0
        for give in gives:
            if give[0] == friend: # 주는 사람일 때
                arr[friends.index(give[1])] += 1 # 받은사람 점수 +1
            if give[1] == friend: # 받느 사람일때
                arr[friends.index(give[0])] -= 1 # 
                
        for i in range(length):
            if arr[i] > 0:
                num += 1
            if arr[i] == 0:
                if give_points[idx] > give_points[i]:
                    num += 1
        answer.append(num)
    
    return max(answer)