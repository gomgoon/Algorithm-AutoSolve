n = int(input())
dic = {}

for _ in range(n):
    age, string = input().split()
    age = int(age)
    if age not in dic:
        dic[age] = [string]
    else:
        dic[age].append(string)
        

key_list = sorted(dic.keys())
for key in key_list:
    for value in dic[key]:
        print(key, value)