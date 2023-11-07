#1
#7 +6
#19 +12
#37 +18
#61 +24
n = int(input())
val = 1
val2 = 6
count = 1
result = 0
while True:
   num = val
   if num >= n:
       result = count
       break
   else:
       count += 1
       val += val2
       val2 += 6
print(result)