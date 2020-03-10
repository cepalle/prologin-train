import heapq

n, m, r = [int(e) for e in input().split()]
lg = []
MA = [[float('inf') if i != j else 0 for i in range(0, n)] for j in range(0, n)]

lg = [[] for _ in range(0, n)]
for _ in range(0, m):
    d, a, t = [int(e) for e in input().split()]
    lg[d - 1].append((a - 1, t))


def dji(d):
    pile = [
        (0, d)
    ]
    while len(pile) > 0:
        h, p = heapq.heappop(pile)
        for (dd, t) in lg[p]:
            if MA[d][dd] > h + t:
                MA[d][dd] = h + t
                heapq.heappush(pile, (h + t, dd))


for _ in range(0, r):
    d, a = (int(e) for e in input().split())
    if MA[d - 1][a - 1] == float('inf'):
        dji(d - 1)
    print(MA[d - 1][a - 1])
