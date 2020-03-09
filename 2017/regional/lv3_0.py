n, k = [int(e) for e in input().split()]
lp = [int(e) for e in input().split()]
lp.sort(key=lambda e: -e)

tot = 0
while len(lp) > 3:
    c1 = None
    while len(lp) > 1 and lp[0] > lp[1] + k:
        lp.pop(0)
    if len(lp) > 1:
        c1 = lp[1]
        lp.pop(0)
        lp.pop(0)
    else:
        break
    c2 = None
    while len(lp) > 1 and lp[0] > lp[1] + k:
        lp.pop(0)
    if len(lp) > 1:
        c2 = lp[1]
        lp.pop(0)
        lp.pop(0)
    else:
        break
    tot += c1 * c2

print(tot)
