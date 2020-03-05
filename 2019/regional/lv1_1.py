n = int(input())
lnb = [int(e) for e in input().split()]

mx = 0
cur = 0
for e in lnb:
    if e == 1:
        cur += 1
    else:
        cur = 0
    mx = max(mx, cur)
print(mx)
