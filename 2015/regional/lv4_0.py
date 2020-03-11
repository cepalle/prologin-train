h, l = [int(e) for e in input().split()]
y, x = [int(e) for e in input().split()]
M = [list(map(int, input().split(' '))) for _ in range(h)]

dd = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
]


def count(p, M):
    colp = M[p[0]][p[1]]
    pile = [
        p
    ]
    tot = 0
    while len(pile) > 0:
        y, x = pile.pop()
        for of in dd:
            dx, dy = of
            nx = dx + x
            ny = dy + y
            if 0 <= nx < l and 0 <= ny < h:
                if M[ny][nx] == colp:
                    pile.append((ny, nx))
                    M[ny][nx] = -1
                elif M[ny][nx] == 2:
                    tot += 1
                    M[ny][nx] = -1

    return tot


print(count((y, x), M))
