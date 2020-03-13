m, n = [int(e) for e in input().split()]
M = [list(input()) for _ in range(0, m)]

dd = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
]


def add_num(p, nb):
    pile = [
        p
    ]
    s = M[p[0]][p[1]]
    M[p[0]][p[1]] = nb
    suf = 1
    while len(pile) > 0:
        y, x = pile.pop()
        for d in dd:
            dy, dx = d
            ny = y + dy
            nx = x + dx
            if 0 <= ny < m and 0 <= nx < n and M[ny][nx] == s:
                M[ny][nx] = nb
                suf += 1
                pile.append((ny, nx))
    return suf


ls = []
nb = 0
for y in range(0, m):
    for x in range(0, n):
        if type(M[y][x]) == str and M[y][x] in "VRJB":
            s = add_num((y, x), nb)
            ls.append(s)
            nb += 1


def get_v(i):
    res = set()
    for y in range(0, m):
        for x in range(0, n):
            if M[y][x] == i:
                for d in dd:
                    dy, dx = d
                    ny = y + dy
                    nx = x + dx
                    if 0 <= ny < m and 0 <= nx < n:
                        res.add(M[ny][nx])

    res.discard(i)
    return res


lg = [set() for _ in range(0, nb)]
for i in range(0, nb):
    lg[i] = get_v(i)


# for l in M:
#   print(l)

# print(lg)
# print(ls)


def get_max(i, h):
    cur = sum(map(lambda e: ls[e], h))
    for d in lg[i]:
        if d not in h and h <= lg[d]:
            cur = max(cur, get_max(d, h | {d}))
    return cur


mx = 0
for i in range(0, nb):
    mx = max(mx, get_max(i, {i}))

print(mx)
