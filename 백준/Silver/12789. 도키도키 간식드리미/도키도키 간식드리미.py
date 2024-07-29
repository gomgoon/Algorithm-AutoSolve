n = int(input())
arr = list(map(int, input().split()))
num = 1
temp = []
sf = 0

for i in range(1, n+1):
    if num != i:
        print("Sad")
        sf=1
        break
    if temp and temp[-1] == num:
        temp.pop()
        num += 1
        continue
    else:
        for j in range(len(arr)):
            nf = 0
            if arr[0] != num:
                temp.append(arr.pop(0))
            else:
                arr.pop(0)
                num +=1
                nf = 1
                break
        if nf == 0:
            print("Sad")
            sf = 1
            break
        
if sf == 0:
    print("Nice")