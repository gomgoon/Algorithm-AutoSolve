s = input()
q = int(input())

for _ in range(q):
    a,l,r = input().split()
    l, r = int(l), int(r)
    sub = s[l:r + 1]
    res = 0
    
    for i in range(len(sub)):
        if sub[i] == a:
            res += 1

    print(res)