def link_to_the_past0(m, n, present, passe):
    l_pos = []
    for y in range(0, m):
        for x in range(0, n):
            if (present[y][x] == "d"):
                present[y][x] = 0
                l_pos.append([y, x, True, 0])
            elif (passe[y][x] == "d"):
                present[y][x] = 0
                l_pos.append([y, x, False, 0])
            if (present[y][x] == "."):
                present[y][x] = float("inf")
            if (passe[y][x] == "."):
                passe[y][x] = float("inf")

    l_of = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    for pos in l_pos:
        for of in l_of:
            if (0 <= pos[0] + of[0] < m and
                    0 <= pos[1] + of[1] < n):
                if (pos[2]):
                    if (present[pos[0] + of[0]][pos[1] + of[1]] == "a"):
                        print(pos[3] + 1)
                        exit(0)
                    elif (present[pos[0] + of[0]][pos[1] + of[1]] != "#" and
                          present[pos[0] + of[0]][pos[1] + of[1]] > pos[3] + 1):
                        present[pos[0] + of[0]][pos[1] + of[1]] = pos[3] + 1
                        l_pos.append([pos[0] + of[0], pos[1] + of[1], pos[2], pos[3] + 1])
                else:
                    if (passe[pos[0] + of[0]][pos[1] + of[1]] == "a"):
                        print(pos[3] + 1)
                        exit(0)
                    elif (passe[pos[0] + of[0]][pos[1] + of[1]] != "#" and
                          passe[pos[0] + of[0]][pos[1] + of[1]] > pos[3] + 1):
                        passe[pos[0] + of[0]][pos[1] + of[1]] = pos[3] + 1
                        l_pos.append([pos[0] + of[0], pos[1] + of[1], pos[2], pos[3] + 1])
        if (pos[2]):
            if (passe[pos[0]][pos[1]] == "a"):
                print(pos[3] + 1)
                exit(0)
            elif (passe[pos[0]][pos[1]] != "#" and
                  passe[pos[0]][pos[1]] > pos[3] + 1):
                passe[pos[0]][pos[1]] = pos[3] + 1
                l_pos.append([pos[0], pos[1], not pos[2], pos[3] + 1])
        else:
            if (present[pos[0]][pos[1]] == "a"):
                print(pos[3] + 1)
                exit(0)
            elif (present[pos[0]][pos[1]] != "#" and
                  present[pos[0]][pos[1]] > pos[3] + 1):
                present[pos[0]][pos[1]] = pos[3] + 1
                l_pos.append([pos[0], pos[1], not pos[2], pos[3] + 1])


(m, n) = list(map(int, input().split()))
br = [None] * m
for bs in range(0, m):
    br[bs] = list(input())
present = br
bv = [None] * m
for bw in range(0, m):
    bv[bw] = list(input())
passe = bv
link_to_the_past0(m, n, present, passe)
print(0)
