from collections import deque

n = int(input())
arr = [i for i in range(1,n+1)]
deq_arr = deque(arr)
while len(deq_arr) > 1:
    deq_arr.popleft()
    num = deq_arr.popleft()
    deq_arr.append(num)
print(deq_arr[0])
