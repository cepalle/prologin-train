# https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
# https://www.geeksforgeeks.org/knapsack-with-large-weights/

from functools import lru_cache

input()
ca = int(input())


def get_wt_val():
    pda = [int(e) for e in input().split()]
    nbpa = int(input())
    lp = []
    for _ in range(0, nbpa):
        lp.append([int(e) - 1 for e in input().split()])

    wt = []
    val = []
    lh = [False for _ in pda]

    for i in range(0, len(pda)):
        if lh[i]:
            continue
        smg = 0
        nbg = 0
        p = [i]
        while len(p) > 0:
            cur = p.pop(-1)
            lh[cur] = True
            smg += pda[cur]
            nbg += 1
            for pr in lp:
                a, b = pr
                if a == cur and not lh[b]:
                    p.append(b)
                    lh[b] = True
                if b == cur and not lh[a]:
                    p.append(a)
                    lh[a] = True

        if smg == 0:
            continue
        if smg <= ca:
            wt.append(smg)
            val.append(nbg)
    return wt, val


wt, val = get_wt_val()

K = [[] for _ in range(len(wt) + 1)]


def get_h(c, lh):
    if len(lh) == 0 or c < lh[0][0] or c > lh[-1][0]:
        return None
    iff = 0
    isup = len(lh) - 1
    while isup - iff > 1:
        mid = (iff + isup) // 2
        if lh[mid][0] == c:
            return lh[mid][1]
        if lh[mid][0] < c:
            iff = mid
        else:
            isup = mid
    if lh[iff][0] == c:
        return lh[iff][1]
    if lh[isup][0] == c:
        return lh[isup][1]

    return None


def knapSack(c, n):
    if n <= 0 or c <= 0:
        return 0
    res = get_h(c, K[n])
    if res is not None:
        return res

    res = knapSack(c, n - 1)

    if wt[n - 1] <= c:
        res = max(
            val[n - 1] + knapSack(c - wt[n - 1], n - 1),
            res
        )
    K[n].append((c, res))
    K[n].sort()
    return res


print(knapSack(ca, len(wt)))
