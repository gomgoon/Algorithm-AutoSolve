n, k = map(int, input().split())
arr = [i for i in range(1,n+1)]
yose = []
cnt = 0
while arr:
    cnt = (cnt + k - 1) % len(arr)
    yose.append(arr.pop(cnt))
print("<" + ", ".join(map(str, yose)) + ">")