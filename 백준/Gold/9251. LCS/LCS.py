"""
def LCS():
    str1 = input()
    str2 = input()
    LENGTH1 = len(str1)
    LENGTH2 = len(str2)

    visited = [-1] * LENGTH1
    visited2 = [False] * LENGTH2
    dp = [0] * LENGTH1

    for i in range(LENGTH1 - 1, -1, -1):
        #print(f"str1: {str1[i]}")
        #print(f"visited: {visited}")
        for j in range(LENGTH2 - 1, -1, -1):
            #print(f"str2: {str2[j]}")
            if str1[i] == str2[j] and not visited2[j]:
                visited[i] = j
                visited2[j] = True
                # 6번 문자에 방문한 나보다 뒤에 문자에 방문한 문자가 있따면
                # 그 문자의 숫자 중 가장 큰 넘버 + 1을 하면 된다
                for k in range(i, LENGTH1):
                    if visited[k] > visited[i]:
                        dp[i] = max(dp[k], dp[i])
                dp[i] += 1
                break
        #print(dp)
    return max(dp) if dp else 0
"""
def LCS():
    str1 = input()
    str2 = input()
    n, m = len(str1), len(str2)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n):
        for j in range(m):
            if str1[i] == str2[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
    
    return dp[n][m]

print(LCS())
