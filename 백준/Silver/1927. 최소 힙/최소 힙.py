import heapq, sys

heap = []
input = sys.stdin.read
data = input().split()
n = int(data[0])

for i in range(1, n + 1):
    x = int(data[i])

    if x == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, x)