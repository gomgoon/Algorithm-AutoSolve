while True:
    temp = []
    a,b,c = map(int, input().split())
    temp.append(a)
    temp.append(b)
    temp.append(c)
    temp.sort()
    if a==0 and b==0 and c==0:
        break
    else:
        if temp[2] >= temp[1] + temp[0]:
            print('Invalid')
        else:
            if temp[2] == temp[1] == temp[0]:
                print('Equilateral')
            elif temp[0] == temp[1] or temp[1] == temp[2] or temp[0] == temp[2]:
                print('Isosceles')
            else:
                print('Scalene')