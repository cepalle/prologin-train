def prt(tab):
    for l in tab:
        for elt in l:
            print(elt, end=" ")
        print()


def find(l, el):
    for i in range(0, len(l)):
        if (l[i] == el):
            return i
    return -1


def diam(g):
    trad = []
    for c in g:
        if (not c["s1"] in trad):
            trad.append(c["s1"])
        if (not c["s2"] in trad):
            trad.append(c["s2"])

    trad.sort()
    for c in g:
        c["s1"] = find(trad, c["s1"])
        c["s2"] = find(trad, c["s2"])

    M = []
    l = [0] * len(trad)
    for i in range(0, len(trad)):
        M.append(list(l))
    for c in g:
        M[c["s1"]][c["s2"]] = 1
        M[c["s2"]][c["s1"]] = 1

    # prt(M)
    # print()

    hys = [float("inf")] * len(M)
    hys[0] = 0
    l_pos = [[0, 0]]
    for pos in l_pos:
        for i in range(0, len(M)):
            if (M[pos[0]][i] and pos[1] + 1 < hys[i]):
                l_pos.append([i, pos[1] + 1])
                hys[i] = pos[1] + 1

    # print(hys)

    to_start = find(hys, max(hys))
    hys = [float("inf")] * len(M)
    hys[to_start] = 0
    l_pos = [[to_start, 0]]
    for pos in l_pos:
        for i in range(0, len(M)):
            if (M[pos[0]][i] and pos[1] + 1 < hys[i]):
                l_pos.append([i, pos[1] + 1])
                hys[i] = pos[1] + 1

    # print(hys)

    return max(hys)


def exploration_urbaine0(n, m, couloirs):
    l_g = []
    while (couloirs != []):
        g = []
        g.append(couloirs[0])
        couloirs.pop(0)
        for c in g:
            i = 0
            while (i < len(couloirs)):
                if (c["s1"] == couloirs[i]["s1"] or
                        c["s1"] == couloirs[i]["s2"] or
                        c["s2"] == couloirs[i]["s1"] or
                        c["s2"] == couloirs[i]["s2"]):
                    g.append(couloirs[i])
                    couloirs.pop(i)
                else:
                    i += 1
        l_g.append(g)

    # prt(l_g)
    # print()

    l_mx = 0
    for l in l_g:
        l_mx = max(l_mx, len(l))

    i = 0
    while (i < len(l_g)):
        if (len(l_g[i]) != l_mx):
            l_g.pop(i)
        else:
            i += 1

    # prt(l_g)

    mx_d = 0
    for g in l_g:
        mx_d = max(mx_d, diam(g))

    if (len(l_g) == 0):
        print("1 0")
        return
    print(len(l_g[0]) + 1, end=" ")
    print(len(l_g[0]) * 2 - mx_d)


(n, m) = list(map(int, input().split()))
couloirs = [None] * m
for i in range(0, m):
    (s1, s2) = list(map(int, input().split()))
    couloirs[i] = {
        "s1": s1,
        "s2": s2}
exploration_urbaine0(n, m, couloirs)
