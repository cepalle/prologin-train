import heapq

n, m, g = [int(e) for e in input().split()]
lat = [int(input()) for _ in range(0, n)]
ld1 = [[int(e) for e in input().split()] for _ in range(0, m)]
ld2 = [[int(e) for e in input().split()] for _ in range(0, g)]

ld1 = list(map(lambda e: [e[0] - 1, e[1] - 1, e[2]], ld1))
lgd1 = [[] for _ in range(0, n)]
for d1 in ld1:
    lgd1[d1[0]].append((d1[1], d1[2]))

ld2 = list(map(lambda e: [e[0] - 1, e[1] - 1, e[2]], ld2))
lgd2 = [[] for _ in range(0, n)]
for d2 in ld2:
    lgd2[d2[0]].append((d2[1], d2[2]))


def djikstra(i):
    his = [float('inf') if i != j else 0 for j in range(0, n)]
    hisgr = [float('inf') if i != j else 0 for j in range(0, n)]
    pile = [
        (0, i, False)
    ]
    while len(pile) > 0:
        h, pos, gr = heapq.heappop(pile)
        for (d, t) in lgd1[pos]:
            nh = h + t + (lat[pos] if not gr else 0)
            if his[d] > nh:
                his[d] = nh
                heapq.heappush(pile, (nh, d, False))
        for (d, t) in lgd2[pos]:
            nh = h + t + (lat[pos] if not gr else 0)
            if hisgr[d] > nh:
                hisgr[d] = nh
                heapq.heappush(pile, (nh, d, True))
    return his


for i in range(0, n):
    res = djikstra(i)
    res.pop(i)
    flt = list(filter(lambda e: e != float('inf'), res))
    if len(flt) > 0:
        print(sum(flt) // len(flt))
    else:
        print(-1)
