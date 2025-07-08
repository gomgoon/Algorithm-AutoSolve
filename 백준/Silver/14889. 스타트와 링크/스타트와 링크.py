import itertools

n = int(input())
person = [i for i in range(n)]
arr = []
LENGTH = n // 2
res = float('inf')

for i in range(n):
    arr.append(list(map(int, input().split())))
a = list(itertools.combinations(person, LENGTH))
b = list(itertools.combinations(person, LENGTH))
b.reverse()
LENGTH = len(a) // 2
for i in range(LENGTH):
    Aresult = 0
    Bresult = 0
    for j in range(len(a[i])):
        for k in range(j + 1, len(a[i])):
            Aresult += arr[a[i][j]][a[i][k]]
            Aresult += arr[a[i][k]][a[i][j]]
            Bresult += arr[b[i][j]][b[i][k]]
            Bresult += arr[b[i][k]][b[i][j]]
    res = min(res, abs(Aresult - Bresult))
print(res)