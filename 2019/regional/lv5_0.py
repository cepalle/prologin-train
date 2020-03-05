nba = int(input())
ca = int(input())
pda = [int(e) for e in input().split()]
nbpa = int(input())
lp = []
for _ in range(0, nbpa):
    lp.append([int(e) - 1 for e in input().split()])

freenb = 0
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
        freenb += nbg
        continue
    if smg <= ca:
        wt.append(smg)
        val.append(nbg)


def knapsack(W, wt, val, n):
    dp = [[0 for i in range(W + 1)] for j in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if wt[i - 1] <= w:
                dp[i][w] = max(val[i - 1] + dp[i - 1][w - wt[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]


print(knapsack(ca, wt, val, len(wt)) + freenb)
