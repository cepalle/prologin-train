v = int(input())
n = int(input())
ln = [int(e) for e in input().split()]


def cal_v(h, ln):
    tot = 0
    for e in ln:
        if e < h:
            tot += h - e
    return tot


bif = min(ln)
bsup = max(ln) + (v // len(ln))
while bsup - bif > 1:
    mid = (bif + bsup) // 2
    if cal_v(mid, ln) < v:
        bif = mid
    else:
        bsup = mid

if cal_v(bif, ln) <= v and cal_v(bif + 1, ln) > v:
    print(bif)
else:
    print(bsup)
