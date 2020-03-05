def libertes0(hauteur, largeur, l, c, matrix):
    l_next = [[c, l]]
    nb = matrix[l][c]
    sum = 0
    for pos in l_next:
        # print(pos)
        matrix[pos[1]][pos[0]] = 3
        l_of = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for of in l_of:
            if (0 <= pos[0] + of[0] < len(matrix[0]) and
                    0 <= pos[1] + of[1] < len(matrix)):
                if (matrix[pos[1] + of[1]][pos[0] + of[0]] == 2):
                    matrix[pos[1] + of[1]][pos[0] + of[0]] = 3
                    sum += 1
                elif (matrix[pos[1] + of[1]][pos[0] + of[0]] == nb):
                    l_next.append([pos[0] + of[0], pos[1] + of[1]])

    return sum


line1 = list(map(int, input().split()))
line2 = list(map(int, input().split()))
hauteur = line1[0]
largeur = line1[1]
l = line2[0]
c = line2[1]
matrix = [list(map(int, input().split())) for i in range(hauteur)]
print("%d" % libertes0(hauteur, largeur, l, c, matrix), end='')
