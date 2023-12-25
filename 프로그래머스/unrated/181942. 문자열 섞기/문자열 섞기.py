def solution(str1, str2):
    answer = ''
    len1 = len(str1)
    for i in range(len1):
        answer += str1[i]
        answer += str2[i]
    return answer