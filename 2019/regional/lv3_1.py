m = int(input())
f = int(input())
lpm = [[int(e) for e in input().split()] for _ in range(0, m)]
lpf = [[int(e) for e in input().split()] for _ in range(0, f)]

lsmf = []
for _ in lpm:
    lsmf.append(0)


def dst(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


for f in lpf:
    mmni = -1
    dstmn = float('inf')
    for i in range(0, len(lpm)):
        if dst(f, lpm[i]) < dstmn:
            mmni = i
            dstmn = dst(f, lpm[i])
    lsmf[mmni] += dstmn

print(max(lsmf))