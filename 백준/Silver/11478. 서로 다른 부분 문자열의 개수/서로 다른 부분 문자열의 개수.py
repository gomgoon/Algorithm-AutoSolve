st = input()
leng = len(st)
arr = []
for i in range(1, leng+1):
    for j in range(leng - i + 1):
        arr.append(st[j : j+i])

print(len(set(arr)))
        
