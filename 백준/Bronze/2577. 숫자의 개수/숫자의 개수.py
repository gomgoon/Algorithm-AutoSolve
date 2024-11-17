res = [0] * 10
a = int(input())
b = int(input())
c = int(input())
numbers = str(a*b*c)
for number in numbers:
    res[int(number)] += 1
for number in res:
    print(number)