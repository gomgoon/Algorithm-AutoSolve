n,m = map(int, input().split())

dic = {}
res = 0

for i in range(n):
    st = input()
    dic[st] = 1

for j in range(m):
    st = input()
    if st in dic.keys():
        dic[st] += 1
        res += 1

sorted_dic = sorted(dic)

print(res)

for i in sorted_dic:
    if dic[i] == 2:
        print(i)