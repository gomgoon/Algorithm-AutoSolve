t = int(input())
for _ in range(t):
    score = input()
    res = 0
    st = 1
    for i in score:
        if i == 'O':
            res += st
            st += 1
        else:
            st = 1
    print(res)