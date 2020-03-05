def emacsaure(m, n, carte):
    nv_lave = -1
    pos = [0, 0]
    while pos[1] + 1 < n:
        if (pos[1] <= nv_lave):
            print(0)
            return

        if (pos[1] + 1 < n and carte[pos[0]][pos[1] + 1] == "."):
            pos[1] += 1
        elif (pos[0] + 1 < m and carte[pos[0] + 1][pos[1]] == "."):
            pos[0] += 1

        if (pos[1] + 1 < n and carte[pos[0]][pos[1] + 1] == "."):
            pos[1] += 1
        elif (pos[0] + 1 < m and carte[pos[0] + 1][pos[1]] == "."):
            pos[0] += 1

        nv_lave += 1

    print(1)


(m, n) = map(int, input().split())
carte = [list(input()) for _ in range(m)]
emacsaure(m, n, carte)
