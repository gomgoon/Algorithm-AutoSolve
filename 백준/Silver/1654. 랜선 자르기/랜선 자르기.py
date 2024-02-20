def binary_search_elec(start, end, res):
    if start > end:
        return res
    mid = (start + end) // 2
    cnt = 0
    for i in lis:
        cnt += i // mid
    if cnt >= m:
        res = mid
        return binary_search_elec(mid + 1, end, res)
    else:
        return binary_search_elec(start, mid - 1, res)
    

n, m = map(int,input().split())
lis = []
res = 0
for i in range(n):
    lis.append(int(input()))
res = binary_search_elec(1, max(lis), res)
print(res)