def tete_baissee(n, carte):
    hys = []
    l_pos = []
    for y in range(0, n):
        hys.append([])
        for x in range(0, n):
            if (carte[y][x] == "T"):
                hys[y].append(0)
                l_pos.append([x, y, 0])
            else:
                hys[y].append(float("inf"))

    for pos in l_pos:
        x = pos[0]
        y = pos[1]
        nb_tour = pos[2]

        # print(pos, hys[y][x])

        l_of = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for of in l_of:
            x_next = x
            y_next = y
            while (0 <= x_next + of[0] and x_next + of[0] < n and
                   0 <= y_next + of[1] and y_next + of[1] < n and
                   carte[y_next + of[1]][x_next + of[0]] != "X"):
                x_next += of[0]
                y_next += of[1]
                if (carte[y_next][x_next] == "M"):
                    print(nb_tour)
                    return

            if (hys[y_next][x_next] > nb_tour + 1):
                l_pos.append([x_next, y_next, nb_tour + 1])
                hys[y_next][x_next] = nb_tour + 1

    """Inserez votre code ici"""


n = int(input())
carte = [list(input()) for _ in range(n)]
tete_baissee(n, carte)
