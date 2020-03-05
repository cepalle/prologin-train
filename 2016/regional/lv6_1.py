# R V J B

# 6 6
# VVVVVV
# VRRJJV
# VRVVJV
# VRVVJV
# VBBBBV
# VVVVVV

def print_tab(tab):
    for l in tab:
        for elt in l:
            print(elt, end="")
        print()
    print()


def cal_cache(m, n, carte, color, y, x, cache):
    carte[y][x] = cache
    sum = 0
    l_of = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    for of in l_of:
        xx = x + of[0]
        yy = y + of[1]
        if (0 <= xx < n and
                0 <= yy < m and
                carte[yy][xx] == color):
            sum += cal_cache(m, n, carte, color, yy, xx, cache)

    return sum + 1


def find_voisin(m, n, carte, y, x, nb, tab):
    if (carte[y][x] != nb):
        if (carte[y][x] != "#"):
            tab[nb][carte[y][x]] = 1
        return

    carte[y][x] = "#"
    l_of = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    for of in l_of:
        xx = x + of[0]
        yy = y + of[1]
        if (0 <= xx < n and
                0 <= yy < m
        ):
            find_voisin(m, n, carte, yy, xx, nb, tab)


def isin_grp(to_do, l_grp):
    for grp in l_grp:
        if (grp == to_do):
            return True
    return False


def add_grp(to_do, i, M):
    for z in to_do:
        if (not M[i][z]):
            return False
    to_do.append(i)
    to_do.sort()  # or set
    return True


def cal_max(M, l_poid, nb_zone):
    """
    print_tab(M)
    print()
    print(l_poid)
    print()
    print("nb_zone", nb_zone)
    print()
    """

    l_grp = [[]]
    mx = 0

    for grp in l_grp:
        # print(grp)
        for i in range(0, nb_zone):
            to_do = list(grp)

            if (not add_grp(to_do, i, M)):
                continue

            if (not isin_grp(to_do, l_grp)):
                l_grp.append(to_do)
                sup = 0
                for z in to_do:
                    sup += l_poid[z]

                if (sup > mx):
                    mx = sup

    return mx


def invasions_gloutonnes(m, n, carte):
    l_poid = []
    nb = 0
    for y in range(0, m):
        for x in range(0, n):
            if (carte[y][x] == "R" or
                    carte[y][x] == "V" or
                    carte[y][x] == "J" or
                    carte[y][x] == "B"
            ):
                poid = cal_cache(m, n, carte, carte[y][x], y, x, nb)
                nb += 1
                l_poid.append(poid)

    tab = []
    for i in range(0, nb):
        tab.append([])
        for j in range(0, nb):
            tab[i].append(0)

    for de in range(0, nb):
        copy_carte = []
        for l in carte:
            copy_carte.append(list(l))

        for y in range(0, m):
            for x in range(0, n):
                if (copy_carte[y][x] == de):
                    find_voisin(m, n, copy_carte, y, x, de, tab)

    # print_tab(carte)

    print(cal_max(tab, l_poid, nb))


(m, n) = list(map(int, input().split()))
carte = [list(input()) for _ in range(m)]
invasions_gloutonnes(m, n, carte)
