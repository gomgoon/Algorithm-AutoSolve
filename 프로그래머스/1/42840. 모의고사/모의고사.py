def solution(answers):
    answer = []
    p = [0] * 3
    sol = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
    for i in range(len(answers)):
        if answers[i] == sol[0][i % 5]:
            p[0] += 1
        if answers[i] == sol[1][i % 8]:
            p[1] += 1
        if answers[i] == sol[2][i % 10]:
            p[2] += 1
    for i in range(3):
        if p[i] == max(p):
            answer.append(i+1)
    return answer