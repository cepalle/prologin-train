n, m = [int(e) for e in input().split()]
lgi = [[int(e) for e in input().split()] for _ in range(0, m)]

lg = [list() for _ in range(0, n)]
for e in lgi:
    u, v, w = e
    lg[u - 1].append([v - 1, w])
    lg[v - 1].append([u - 1, w])


def dijkstra_memo(d, memo):
    memo[d] = 0
    pile = [
        [d, 0]
    ]
    while len(pile) > 0:
        # print(pile)
        cd, cw = pile.pop(-1)

        for dst in lg[cd]:
            fd, fw = dst
            nw = cw + fw
            if memo[fd] >= nw:
                memo[fd] = nw
                pile.append([fd, nw])
        pile.sort(key=lambda e: -e[1])


memo = [float('inf') for x in range(0, n)]
memo_test = [[float('inf') for x in range(0, n)] for _ in range(0, n)]
sm = 0
for dd in range(0, n):
    for i in range(0, n):
        memo[i] = float('inf')
    dijkstra_memo(dd, memo)
    for e in memo:
        if e != float('inf'):
            sm += e

print(sm)
