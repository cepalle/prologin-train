class hyst:
    tab = []


def traversee_du_desert_aux(k, n, desert, pos):
    if (pos >= n):
        return 0

    if (hyst.tab[pos] != -2):
        return hyst.tab[pos]

    min_no_saut = -1
    if (pos + 1 == n or pos + 1 < n and desert[pos + 1] != "#"):
        min_no_saut = traversee_du_desert_aux(k, n, desert, pos + 1)

    can_saut = True
    for i in range(1, k + 1):
        if (pos + i < n and desert[pos + i] == "^"):
            can_saut = False

    if (pos + k < n and desert[pos + k] == "#"):
        can_saut = False

    min_saut = -1
    if (can_saut):
        min_saut = traversee_du_desert_aux(k, n, desert, pos + k)
        if (min_saut != -1):
            min_saut += 1

    if (min_no_saut == -1 or min_saut == -1):
        hyst.tab[pos] = max(min_saut, min_no_saut)
    else:
        hyst.tab[pos] = min(min_saut, min_no_saut)

    # print(pos, hyst.tab[pos])
    return hyst.tab[pos]


def traversee_du_desert(k, n, desert):
    pos = 0
    for i in range(0, n):
        hyst.tab.append(-2)
        if (desert[i] == "R"):
            pos = i

    print(traversee_du_desert_aux(k, n, desert, pos))


k = int(input())
n = int(input())
desert = list(input())
traversee_du_desert(k, n, desert)
