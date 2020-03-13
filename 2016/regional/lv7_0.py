#        20   1    23   951
#      5    25   26   49   1000
# 5    X    30   31   54   1005
# 25        X    51   74   1025
# 26             X    75   1026
# 49                  X    1049
# 1000                     X

#      |  25   14   2    7
#      |8    33   47   49   56
#      |-----------------------
# 8    |X    41   55   57   64
# 33   |     X    80   82   89
# 47   |          X    96   103
# 49   |               X    105
# 56   |                    X

# 5
# 30 31 54 1005 51 74 1025 75 1026 1049

n = int(input())
ne = int(n * (n - 1) / 2)
le = [int(e) for e in input().split()]
le.sort()

lp = [[None for _ in range(0, i + 1)] for i in range(0, n - 1)]


def check_lp(lp):
    for j in range(0, len(lp) - 1):
        dd = None
        for i in range(0, len(lp[j])):
            if lp[j][i] is None or lp[j + 1][i] is None:
                return True
            if lp[j + 1][i] < lp[j][i]:
                return False
            if i > 0 and lp[j][i - 1] > lp[j][i]:
                return False
            if dd is None:
                dd = lp[j + 1][i] - lp[j][i]
            else:
                if lp[j + 1][i] - lp[j][i] != dd:
                    return False
    return True


def backtrack(lr, lp, ic, jc):
    # print(jc, ic)
    nic = ic + 1
    njc = jc
    if nic > njc:
        njc = nic
        nic = 0
    # for l in lp:
    #    print(l)
    if len(lr) == 0:
        return lp
    for i in range(0, len(lr)):
        cur = lr.pop(0)
        if (ic == 0 or lp[jc][ic - 1] <= cur) and (jc == 0 or ic >= len(lp[jc - 1]) or lp[jc - 1][ic] <= cur):
            lp[jc][ic] = cur
            if check_lp(lp):
                res = backtrack(lr, lp, nic, njc)
                if res is not None:
                    return res
            lp[jc][ic] = None
        lr.append(cur)
    return None


res = backtrack(le, lp, 0, 0)
if res is not None:
    # for l in res:
    #    print(l)
    ld = []
    for j in range(0, len(lp) - 1):
        ld.append(lp[j + 1][0] - lp[j][0])
    ld.insert(0, lp[-1][1] - lp[-1][0])

    frst = (lp[0][0] - ld[0]) // 2
    print(frst)
    for d in ld:
        frst += d
        print(frst)
