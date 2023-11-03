numList = []
resultList = []
endPoint=10
for _ in range(10):
    n=int(input())
    numList.append(n % 42)
numList = set(numList)
numLiset = list(numList)
print(f"{len(numLiset)}")
