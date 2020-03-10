# https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
# https://www.geeksforgeeks.org/knapsack-with-large-weights/

nba = int(input())
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
n = len(wt)

dp = [[None for _ in range(n)]
      for _ in range(ca + 1)]


def solveDp(r, i):
    if r <= 0:
        return 0
    if i == n:
        return float('inf')
    if dp[r][i] is not None:
        return dp[r][i]

    dp[r][i] = min(
        solveDp(r, i + 1),
        wt[i] + solveDp(r - val[i], i + 1)
    )
    return dp[r][i]


def maxWeight():
    for i in range(ca, -1, -1):
        if solveDp(i, 0) <= ca:
            return i

    return 0


print(maxWeight())
