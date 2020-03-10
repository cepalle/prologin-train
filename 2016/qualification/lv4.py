import math

n = int(input())
lp = []
for _ in range(0, n):
    x, y = [int(e) for e in input().split()]
    lp.append((x, y))


def dst(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


count = [float('inf') for _ in range(0, n)]
pred = [None for _ in range(0, n)]

count[0] = 0
F = list(range(0, n))
F.sort(key=lambda e: -count[e])

while len(F) > 0:
    t = F.pop()
    for u in F:
        d = dst(lp[t], lp[u])
        if count[u] >= d:
            pred[u] = t
            count[u] = d
    F.sort(key=lambda e: -count[e])

tot = 0
for i in range(0, n):
    if pred[i] is not None:
        tot += dst(lp[i], lp[pred[i]])

print(int(tot))
