def solution(n, computers):
    visit = [False for i in range(n)]
    answer = 0
    for idx, i in enumerate(visit):
        if i == False:
            check_network(visit, n, computers, idx)
            answer+=1
    return answer

def check_network(visit, n, computers, idx):
    visit[idx] = True
    for idx2, i in enumerate(computers[idx]):
        if visit[idx2] == False and i == 1:
            visit[idx2] = True
            connect_network(visit, n, computers, idx2)

def connect_network(visit, n, computers, idx):
    computer = computers[idx]
    for idx2, i in enumerate(computer):
        if visit[idx2] == False and i == 1:
            visit[idx2] = True
            connect_network(visit, n, computers, idx2)