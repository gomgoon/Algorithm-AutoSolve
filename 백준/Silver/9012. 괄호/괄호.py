k = int(input())

for _ in range(k):
    stack = []
    nf = 0
    bracket = input()
    for i in bracket:
        if i == '(':
            stack.append(1)
        if i == ')':
            if stack:
                stack.pop()
            else:
                nf = 1
                break

    if stack:
        print('NO')
    else:
        if nf == 1:
            print('NO')
        else:
            print('YES')