sum = 0.0
sumPoint = 0.0
for _ in range(20):
    obj, point, grade = input().split()
    point=float(point)
    if grade == 'A+': sum += point*4.5
    elif grade == 'A0': sum += point*4.0
    elif grade == 'B+': sum += point*3.5
    elif grade == 'B0': sum += point*3.0
    elif grade == 'C+': sum += point*2.5
    elif grade == 'C0': sum += point*2.0
    elif grade == 'D+': sum += point*1.5
    elif grade == 'D0': sum += point*1.0
    elif grade == 'F': sum += point*0.0
    else:   
        continue
    sumPoint += point

if sumPoint == 0:
    print(sum)
else:
    print(sum/sumPoint)