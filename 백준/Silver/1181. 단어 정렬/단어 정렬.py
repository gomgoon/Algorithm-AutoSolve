n = int(input())
strings = []

for _ in range(n):
    string = input()
    if string not in strings:
        strings.append(string)

strings.sort(key = lambda string: (len(string), string) )
for string in strings:
    print(string)


'''
13
but
i
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours
'''