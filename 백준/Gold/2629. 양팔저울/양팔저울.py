n = int(input())
weight = list(map(int, input().split()))
m = int(input())
bead = list(map(int, input().split()))

dic = {}
for num in weight:
    key = list(dic.keys())
    for k in key:
        dic[k + num] = 1
        dic[k - num] = 1
        dic[num - k] = 1
    dic[num] = 1

for b in bead:
    if b in dic.keys():
        print('Y', end = ' ')
    else:
        print('N', end = ' ')
    