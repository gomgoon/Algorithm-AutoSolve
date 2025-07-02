n = int(input())
arr = []
dic = {"ChongChong": 1}
res = 0

for i in range(n):
    str1, str2 = input().split()
    if str1 not in dic:
        dic[str1] = 0
    if str2 not in dic:
        dic[str2] = 0
    
    if dic[str1] == 1 or dic[str2] == 1:
        dic[str1] = 1
        dic[str2] = 1

res = 0
for key in dic:
    if dic[key] == 1:
        res += 1
print(res)