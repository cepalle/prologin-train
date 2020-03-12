nc, nt, ni = [int(e) for e in input().split()]
lt = [[int(e) for e in input().split()] for _ in range(0, nt)]
li = [[int(e) for e in input().split()] for _ in range(0, ni)]

lg = [[] for _ in range(0, nc)]

for t in lt:
    lg[t[1]].append(t[0])
    lg[t[0]].append(t[1])


def check_couverture(lg):
    his = set()
    pile = [
        0
    ]
    while len(pile) > 0:
        cur = pile.pop()
        for d in lg[cur]:
            if d not in his:
                his.add(d)
                pile.append(d)
    return len(his) == nc


def brut(i, lg):
    if i == ni:
        return check_couverture(lg)
    t1 = lt[li[i][0]]
    t2 = lt[li[i][1]]

    lg[t1[0]].remove(t1[1])
    lg[t1[1]].remove(t1[0])
    lg[t2[0]].remove(t2[1])
    lg[t2[1]].remove(t2[0])
    if not check_couverture(lg):
        lg[t1[0]].append(t1[1])
        lg[t1[1]].append(t1[0])
        lg[t2[0]].append(t2[1])
        lg[t2[1]].append(t2[0])
    else:
        return brut(i + 1, lg)

    lg[t1[0]].remove(t1[1])
    lg[t1[1]].remove(t1[0])
    if not check_couverture(lg) or not brut(i + 1, lg):
        return False
    lg[t1[0]].append(t1[1])
    lg[t1[1]].append(t1[0])

    lg[t2[0]].remove(t2[1])
    lg[t2[1]].remove(t2[0])
    if not check_couverture(lg) or not brut(i + 1, lg):
        return False
    lg[t2[0]].append(t2[1])
    lg[t2[1]].append(t2[0])
    return True


print(1 if brut(0, lg) else 0)
