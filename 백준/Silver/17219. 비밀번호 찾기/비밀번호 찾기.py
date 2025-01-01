n, m = map(int, input().split())
dic = {}
for i in range(n):
    st1, st2 = input().split()
    dic[st1] = st2
for i in range(m):
    st = input()
    print(dic[st])