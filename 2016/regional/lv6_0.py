m, n = [int(e) for e in input().split()]
M = [list(input()) for _ in range(0, m)]

dd = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1)
]


def del_v(p):
    pile = [
        p
    ]
    M[p[0]][p[1]] = "#"
    while len(pile) > 0:
        y, x = pile.pop()
        for ds in dd:
            dx, dy = ds
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and M[ny][nx] in ".v":
                M[ny][nx] = "#"
                pile.append((ny, nx))
            if 0 <= nx < n and 0 <= ny < m and M[ny][nx] == "?":
                M[ny][nx] = "#"
            if 0 <= nx < n and 0 <= ny < m and M[ny][nx] == "c":
                M[ny][nx] = "#"
                return True
            if nx < 0 or nx == n or ny < 0 or ny == m:
                return True
    return False


def del_c(p):
    pile = [
        p
    ]
    M[p[0]][p[1]] = "#"
    while len(pile) > 0:
        y, x = pile.pop()
        for ds in dd:
            dx, dy = ds
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and M[ny][nx] in ".c?":
                M[ny][nx] = "#"
                pile.append((ny, nx))
    return False


def main():
    for i in range(0, m):
        for j in range(0, n):
            if M[i][j] == "v":
                if del_v((i, j)):
                    print(0)
                    return

    # for l in M:
    #    print(l)
    # print()
    for i in range(0, m):
        if M[i][n - 1] != "#":
            del_c((i, n - 1))
        if M[i][0] != "#":
            del_c((i, 0))
    for i in range(0, n):
        if M[0][i] != "#":
            del_c((0, i))
        if M[m - 1][i] != "#":
            del_c((m - 1, i))

    # for l in M:
    #    print(l)
    for l in M:
        if "c" in l:
            print(0)
            return
    print(1)


main()
