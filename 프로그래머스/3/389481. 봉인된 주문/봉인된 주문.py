def solution(n, bans):
    a = 'abcdefghijklmnopqrstuvwxyz'
    dic = {}
    for idx, i in enumerate(a):
        dic[i] = idx + 1
    
    nums = []
    for ban in bans:
        num = 0
        for char in ban:
            num = num * 26 + dic[char]
        nums.append(num)
    
    nums.sort()
    for num in nums:
        if num <= n:
            n += 1
        else:
            break
    
    r = []
    while n > 0:
        n -= 1
        r.append(n % 26)
        n //= 26
    
    answer = ''
    for char in reversed(r):
        answer += chr(ord('a') + char)
    
    return answer