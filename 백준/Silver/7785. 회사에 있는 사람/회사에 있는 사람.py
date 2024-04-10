# BOJ 7785 회사에 있는 사람

n = int(input())
arr = []

for i in range(n):
    st = input().split()
    if st[1] == 'enter':
        arr.append(st[0])
    else:
        arr.remove(st[0])
        

set_arr = list(set(arr))
set_arr.sort(reverse=True)
for i in set_arr:
    print(i)