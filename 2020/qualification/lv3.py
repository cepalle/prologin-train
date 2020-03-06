input()
lp = [int(e) for e in input().split()]
b = int(input())

iif = 0
sup = 0
cur = 0
nbmin = float('inf')
while sup < len(lp) and iif < len(lp):
    cur += lp[sup]
    sup += 1
    while cur > b:
        cur -= lp[iif]
        iif += 1
    if cur == b:
        while lp[iif] == 0:
            iif += 1
        nbmin = min(sup - iif, nbmin)

if nbmin != float('inf'):
    print(nbmin)
else:
    print(-1)
