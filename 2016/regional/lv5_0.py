def vimetrodon(m, n, carte):
    tab = []
    for i in range(0, m):
        tab.append([])
        for j in range(0, n):
            tab[i].append(float("inf"))

    tab[0][0] = 0
    lpos = [[0, 0, 0]]
    for pos in lpos:
        x = pos[0]
        y = pos[1]
        nb_tour = pos[2]
        if (n <= x + 1):
            print(1)
            return

        nv_lave_next = int(int(nb_tour + 1) / int(2))
        l_of = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for of in l_of:
            if (0 <= x + of[0] and x + of[0] < n and
                    0 <= y + of[1] and y + of[1] < m and
                    carte[y + of[1]][x + of[0]] == "." and
                    tab[y + of[1]][x + of[0]] > nb_tour + 1 and
                    nv_lave_next <= x + of[0]):
                tab[y + of[1]][x + of[0]] = nb_tour + 1
                lpos.append([x + of[0], y + of[1], nb_tour + 1])
                # print(pos, of, nv_lave_next)

    print(0)
    """Inserez votre code ici"""


(m, n) = list(map(int, input().split()))
carte = [list(input()) for _ in range(m)]
vimetrodon(m, n, carte)
