from collections import Counter

n = int(input())
arr = []

for i in range(n):
    num = int(input())
    arr.append(num)
arr.sort()

print(round(sum(arr) / n))
print(arr[n//2])

count = Counter(arr).most_common()
if len(count) > 1 and count[0][1] == count[1][1]:
    print(sorted([x[0] for x in count if x[1] == count[0][1]])[1])
else:
    print(count[0][0])

print(arr[-1] - arr[0])