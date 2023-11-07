n = int(input())
for _ in range(n):
    num = float(input())
    quarter = 0
    daim = 0
    nikel = 0
    pennie = 0
    while num >= 25:
        num -= 25
        quarter += 1
    while num >= 10:
        num -= 10
        daim += 1
    while num >= 5:
        num -= 5
        nikel += 1
    while num >= 1:
        num -= 1
        pennie += 1
    print(f"{quarter} {daim} {nikel} {pennie}")