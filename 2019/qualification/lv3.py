n, m = [int(e) for e in input().split()]
la = [int(e) for e in input().split()]
la.sort()

iff = 0
sup = 0
mx = 0
while sup < len(la) and iff < len(la):
    while sup < len(la) and la[sup] <= la[iff] + m:
        sup += 1
    mx = max(mx, sup - iff)
    iff += 1

print(mx)
