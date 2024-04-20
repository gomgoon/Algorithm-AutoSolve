n,m = map(int, input().split())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

dic = {}

for i in arr1:
    dic[i] = 1

for i in arr2:
    if i in dic.keys():
        dic[i] += 1

res = 0
for i in dic:
    if dic[i] == 2:
        res += 1

print(len(set(arr1+arr2)) - res)