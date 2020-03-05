def cacher(carte, pos, alt):
    carte[pos[1]][pos[0]] = -1
    sum = 1
    l_of = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    for of in l_of:
        if (0 <= pos[0] + of[0] < len(carte[0]) and
                0 <= pos[1] + of[1] < len(carte) and
                carte[pos[1] + of[1]][pos[0] + of[0]] == alt):
            sum += cacher(carte, [pos[0] + of[0], pos[1] + of[1]], alt)

    return sum


def manoir_en_relief0(longueur, largeur, carte):
    mx = 0
    for x in range(0, largeur):
        for y in range(0, longueur):
            if (carte[y][x] != -1):
                sup = cacher(carte, [x, y], carte[y][x])
                if (sup > mx):
                    mx = sup
    return mx


(longueur, largeur) = list(map(int, input().split()))
carte = [list(map(int, input().split())) for i in range(longueur)]
print("%d\n" % (manoir_en_relief0(longueur, largeur, carte)), end='')
