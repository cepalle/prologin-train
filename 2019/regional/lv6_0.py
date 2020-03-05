n = int(input())
m = int(input())
# [xi, yi, pi, di]
lg = [[int(e) for e in input().split()] for _ in range(0, m)]
lg = list(map(lambda e: [e[0] - 1, e[1] - 1, e[2], e[3]], lg))

prdp = 1
dstp = set()
for e in lg:
    dstp.add(e[2])
dstp = list(dstp)
dstp.sort()
for e in dstp.__reversed__():
    if prdp % e != 0:
        prdp *= e

g = []

for i in range(0, n):
    dst = []
    for a in lg:
        xi, yi, pi, di = a
        if xi == i:
            dst.append([yi, pi, di])
        if yi == i:
            dst.append([xi, pi, di])

    g.append(dst)

his = {}


def bfs():
    pile = [
        [0, 0]
    ]
    key = str(0) + " " + str(0)
    his[key] = True
    while len(pile) > 0:
        p, h = pile.pop(0)
        # print(p, h)
        if p == n - 1:
            return h
        for a in g[p]:
            yi, pi, di = a
            if di > h or (h - di) % pi != 0:
                continue
            # kh = h + 1 if h + 1 < dmx else dmx + ((h + 1 - dmx) % prdp)
            kh = (h + 1) % prdp
            ky = str(yi) + " " + str(kh)
            if ky not in his:
                pile.append([yi, h + 1])
                his[ky] = True
    return None


res = bfs()
if res is None:
    print('IMPOSSIBLE')
else:
    print(res)