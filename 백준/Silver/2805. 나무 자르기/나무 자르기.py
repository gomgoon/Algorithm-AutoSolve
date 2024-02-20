def binary_search_tree(arr, num, start, end):
    global res
    if start > end:
        return 0
    
    mid = (start + end) // 2
    cut_tree = 0
    
    for tree in arr:
        if tree > mid:
            cut_tree += tree - mid
    
    if cut_tree < num:
        binary_search_tree(arr, num, start, mid - 1)
    else:
        res = mid
        binary_search_tree(arr, num, mid + 1, end)
 
    
res = 0
n, m = map(int,input().split())
trees = list(map(int, input().split()))
binary_search_tree(trees, m, 1, max(trees))
print(res)