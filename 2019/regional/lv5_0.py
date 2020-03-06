# https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
# https://www.geeksforgeeks.org/knapsack-with-large-weights/

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

K = [[None for _ in range(ca + 1)] for _ in range(len(wt) + 1)]


def knapSack(c, n):
    if n <= 0 or c <= 0:
        return 0
    if K[n][c] is not None:
        return K[n][c]

    res = knapSack(c, n - 1)

    if wt[n - 1] <= c:
        res = max(
            val[n - 1] + knapSack(c - wt[n - 1], n - 1),
            res
        )
    K[n][c] = res
    return res


print(knapSack(ca, len(wt)))
