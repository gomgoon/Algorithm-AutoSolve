ascending = '12345678'
descending = '87654321'
res = ''
a = input().split()
for i in a:
    res += i
if res == ascending:
    print('ascending')
elif res == descending:
    print('descending')
else:
    print('mixed')