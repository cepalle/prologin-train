n = int(input())
ln = [0] + [int(input()) for _ in range(0, n - 1)]

lg = [set()] + [set() for _ in range(0, n - 1)]

for i in range(1, n):
    lg[ln[i]].add(i)


def dfs_depth(i, p):
    if p < 0:
        return 0
    if p == 0:
        return 1
    res = 0
    for e in lg[i]:
        res += dfs_depth(e, p - 1)
    return res


def count(i, p):
    le = []
    for e in lg[i]:
        le.append(dfs_depth(e, p - 1))
    res = 0
    while len(le) > 0:
        cur = le.pop()
        res += cur * sum(le)
    return res


for p in range(1, 11):
    tot = 0
    for i in range(0, n):
        tot += count(i, p)
    print(tot)
