from collections import Counter

def solution(nums):
    temp = len(nums)
    maxnum = temp / 2
    mon = len(list(Counter(nums).keys()))
    if mon <= maxnum:
        answer = mon
    else:
        answer = maxnum
    return answer