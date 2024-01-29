def solution(genres, plays):
    dic = {}
    res = []
    total_dic = {}
    answer = []
    # {장르: [재생횟수, 고유번호], 장르: [재생횟수, 고유번호]}
    for i in range(len(genres)):
        if genres[i] not in dic:
            dic[genres[i]] = [(plays[i], i)]
        else:
            dic[genres[i]].append((plays[i], i))

    # 각 genre당 총재생횟수 저장
    for genre in dic:
        temp = 0
        for i in range(len(dic[genre])):
            temp += dic[genre][i][0]
        total_dic[genre] = temp
    
    sorted_total_dic = sorted(total_dic.items(), key=lambda x: x[1], reverse=True)
                
    for genre in dic:
        dic[genre] = sorted(dic[genre], key=lambda x: x[0], reverse=True)
    
    print(dic)
    print(sorted_total_dic)
    for k in sorted_total_dic:
        print(dic[k[0]])
        length = 2 if len(dic[k[0]]) >= 2 else 1
        for i in range(length):
            answer.append(dic[k[0]][i][1])
            
    print(answer)
    
    return answer