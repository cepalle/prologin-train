n = int(input())
ln = [int(e) for e in input().split()]

lg = [set() for _ in range(0, n)]
for i in range(0, n):
    lg[ln[i]].add(i)
    lg[i].add(ln[i])

lg2 = []
for i in range(0, n):
    lg2.append((i, lg[i]))

lg2.sort(key=lambda e: -len(e[1]))

tot = 0

while len(lg2) > 0:
    si = set()
    ss = set()
    for (i, s) in lg2:
        if len(s) == 1 and i not in ss:
            si.add(i)
            ss |= s

    if len(si) == 0:
        if len(lg2) > 0 and len(lg2[-1][1]) > 2:
            lg2.sort(key=lambda c: -len(c[1]))
        i, s = lg2[-1]
        si.add(i)
        ss = s

    lg2 = list(map(lambda e: (e[0], e[1] - ss), filter(lambda e: e[0] not in si and len(si & e[1]) == 0, lg2)))

    tot += len(si)

print(tot)
