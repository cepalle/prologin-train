n = int(input())

mxb = 0
mxc = 0
for _ in range(0, n):
    lo, la = [int(e) for e in input().split()]
    if lo >= 2 * la:
        mxb = max(mxb, lo)
    else:
        mxc = max(mxc, lo)
if mxc > mxb:
    print('C')
else:
    print('B')
