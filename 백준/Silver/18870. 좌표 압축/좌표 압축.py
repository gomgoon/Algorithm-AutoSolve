import sys

input = sys.stdin.readline

n = int(input())
lis = list(map(int,input().split()))
sorted_lis = sorted(list(set(lis)))

dic = {sorted_lis[i] : i for i in range(len(sorted_lis))}
for i in lis:
    print(dic[i], end=' ')