global res
res = 0

def solution(numbers, target):
    global res
    bfs(numbers, target, 0, [])
    
    return res

def bfs (numbers, target, depth, nums):
    if depth == len(numbers):
        num = sum(nums)
        if num == target:
            global res
            res+=1
        return;
    bfs(numbers, target, depth + 1, nums + [numbers[depth]])
    bfs(numbers, target, depth + 1, nums + [-numbers[depth]])
    
    