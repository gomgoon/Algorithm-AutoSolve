n = int(input())
arr = []
dic = {}
res = 0

for i in range(n):
    arr.append(input())
    if arr[i] == 'ENTER':
        dic = {}
    elif arr[i] not in dic:
        res += 1
        dic[arr[i]] = 1
print(res)