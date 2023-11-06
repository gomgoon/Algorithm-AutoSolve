strArray = input()
result=0
croCharset = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in croCharset:
    strArray = strArray.replace(i, '1')
print(len(strArray))        