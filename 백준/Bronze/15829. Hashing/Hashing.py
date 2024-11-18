m = 1234567891
l = int(input())
string = input()
res = 0

for idx, s in enumerate(string):
    n = ord(s) - ord('a') + 1
    res += n * (31 ** (idx))
    res %= m

print(res)