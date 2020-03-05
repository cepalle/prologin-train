n, p = [int(e) for e in input().split()]
m = int(input())
ld = [int(input()) for _ in range(0, m)]

nbsu = len(list(filter(lambda e: e == 0, ld)))
nbsa = len(list(filter(lambda e: e == 1, ld)))
nbn = len(list(filter(lambda e: e == 2, ld)))

nbi = 0

if n < nbsu:
    nbi += (nbsu - n)
    n = 0
else:
    n -= nbsu

if p < n:
    nbi += (nbsa - p)
    p = 0
else:
    p -= nbsa

if n + p < nbn:
    nbi += (nbn - n - p)

print(nbi)
