t = int(input())
n = int(input())
planetes = [dict(zip(("x", "y", "k"), map(int, input().split()))) for _ in range(n)]
d = int(input())
mission_k = list(map(int, input().split()))

lpk = [[] for _ in range(0, t)]
for i in range(0, len(planetes)):
    lpk[planetes[i]['k']].append(i)


def dstp(p1, p2):
    return abs(p1['x'] - p2['x']) + abs(p1['y'] - p2['y'])


dp = [[None for _ in range(0, len(mission_k))] for _ in range(0, len(planetes))]


def search(ip, im):
    if im == len(mission_k):
        return 0

    if dp[ip][im] is not None:
        return dp[ip][im]

    mn = float('inf')
    for idst in lpk[mission_k[im]]:
        mn = min(
            mn,
            dstp(planetes[ip], planetes[idst]) + search(idst, im + 1)
        )
    dp[ip][im] = mn
    return mn


mnd = float('inf')
for i in lpk[mission_k[0]]:
    mnd = min(mnd, search(i, 1))

print(mnd)
