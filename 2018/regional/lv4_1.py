n, k = [int(e) for e in input().split()]
lc = []
for _ in range(0, n):
    m = int(input())
    lc.append([int(e) for e in input().split()])

memo = {}


def brut(i, tot):
    if tot >= k:
        return -1
    if i == len(lc):
        return tot
    key = str(i) + " " + str(tot)
    if key in memo:
        return memo[key]

    mx = -1
    for c in lc[i]:
        mx = max(mx, brut(i + 1, tot + c))

    memo[key] = mx
    return mx


print(brut(0, 0))
