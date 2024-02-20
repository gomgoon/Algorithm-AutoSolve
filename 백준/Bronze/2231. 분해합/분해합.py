n = int(input())
arr = []
answer = 0
for i in range(1, n):
    st = str(i)
    temp = i
    for j in st:
        temp += int(j)
    if temp == n:
        print(i)
        answer = 1
        break
if answer == 0:
    print(0)