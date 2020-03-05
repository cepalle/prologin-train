n = int(input())
v = float(input())

mxv = -1
mxi = -1
for i in range(0, n):
    lv = [float(e) for e in input().split()]
    smv = sum(lv)
    # smt = sum(list(map(lambda e: 1/e, lv)))
    if v >= smv > mxv:
        mxi = i
        mxv = smv
print(mxi)
