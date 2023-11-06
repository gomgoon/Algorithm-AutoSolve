strArray = input()
strArray = strArray.upper()
setStrArray = set(strArray)
setStrArray = list(setStrArray)

countList = []
for i in setStrArray:
    countList.append(strArray.count(i))
if countList.count(max(countList)) > 1:
    print('?')
else:
    print(setStrArray[countList.index(max(countList))])