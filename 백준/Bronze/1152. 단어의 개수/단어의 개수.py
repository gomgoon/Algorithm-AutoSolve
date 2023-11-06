strArray=input()
blankCount = strArray.count(' ') + 1
if strArray[0] == ' ': blankCount -= 1
if strArray[-1] == ' ': blankCount -= 1
print(blankCount)