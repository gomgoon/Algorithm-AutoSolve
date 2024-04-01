n = int(input())
dic = {}

for _ in range(n):
    y,x = map(int, input().split())
    if x not in dic:
        dic[x] = [y]
    else:
        dic[x].append(y)

for key in dic.keys():
    dic[key] = sorted(dic[key])

sorted_dic = dict(sorted(dic.items(), key=lambda item: item[0]))

for key, values in sorted_dic.items():
    for value in values:
        print(value, key)