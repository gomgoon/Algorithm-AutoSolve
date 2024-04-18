n,m = map(int, input().split())

arr = []
count_dic = {}

for i in range(1,n+1):
    string = input()
    arr.append(string)
    count_dic[string] = i

for _ in range(m):
    string = input()
    if (string[0] >= 'a' and string[0] <= 'z') or (string[0] >= 'A' and string[0] <= 'Z'):
        print(count_dic[string])
    else:
        print(arr[int(string) - 1])