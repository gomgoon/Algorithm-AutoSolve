numberList = list(range(1,30+1))
for _ in range(28):
    idx=int(input())
    numberList[idx-1]=0
for i in range(0,30):
    if numberList[i] != 0:
        print(f"{numberList[i]}")