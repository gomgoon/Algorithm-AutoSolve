import sys
input = sys.stdin.readline
print = sys.stdout.write

s = input().strip()
q = int(input())
prefix = [[0] * (len(s) + 1) for _ in range(26)]

for i in range(len(s)):
    idx = ord(s[i]) - ord('a')
    for j in range(26):
        prefix[j][i + 1] = prefix[j][i]
    prefix[idx][i + 1] += 1

for _ in range(q):
    a, l, r = input().split()
    l, r = int(l), int(r)
    n = ord(a) - ord('a')
    print(str(prefix[n][r + 1] - prefix[n][l]) + '\n')
