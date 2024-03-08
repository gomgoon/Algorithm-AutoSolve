a,b,c = map(int, input().split())
temp = []
temp.append(a)
temp.append(b)
temp.append(c)
temp.sort()
if temp[0] + temp[1] <= temp[2]:
    print(2 * (temp[0] + temp[1]) - 1)
else:
    print(temp[0] + temp[1] + temp[2])