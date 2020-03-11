import heapq

n, m = [int(e) for e in input().split()]

lg = [[] for _ in range(0, n)]
mxl = 0
for _ in range(0, m):
    a, b, l = [int(e) for e in input().split()]
    mxl = max(mxl, l)
    lg[a].append((b, l))
    lg[b].append((a, l))

dp = [[] for _ in range(0, n + 1)]


def get_h(l, hh):
    for h in hh:
        if l == h[0]:
            return h[1]
    return None


def dfs(i, l):
    h = get_h(l, dp[i])
    if h is not None:
        return h

    mx = 0
    for (d, t) in lg[i]:
        if t > l:
            mx = max(mx, 1 + dfs(d, t))
    dp[i].append((l, mx))
    return mx


mx = 0
for i in range(0, n):
    mx = max(mx, dfs(i, 0))
print(mx)
