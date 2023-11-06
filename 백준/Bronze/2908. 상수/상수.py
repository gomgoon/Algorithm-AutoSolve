a,b = input().split()
a = list(a)
a.reverse()
b = list(b)
b.reverse()
a = ''.join(a)
b = ''.join(b)
if int(a) >= int(b):
    print(a)
else:
    print(b)