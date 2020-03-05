#!/usr/bin/env python3

def cherche(lEmp, dep):
    lDepTime = list(lEmp[1][dep])
    while False in lEmp[2][dep]:
        idMin = lDepTime.index(min(lDepTime))
        for dest in lEmp[0][idMin]:
            if not lEmp[2][dep][dest[0]]:
                lEmp[1][dep][dest[0]] = min(dest[1] + lEmp[1][dep][idMin], lEmp[1][dep][dest[0]])
                lDepTime[dest[0]] = min(dest[1] + lEmp[1][dep][idMin], lEmp[1][dep][dest[0]])
        lDepTime[idMin] = float("infinity")
        lEmp[2][dep][idMin] = True


def expert_itinerant(n, m, r, lD, lA, lT, ld, la):
    lEmp, lLigng, lLignd = [[], [], []], [], []
    for x in range(0, n):
        lLigng.append(False)
        lLignd.append(float("infinity"))
    for x in range(0, n):
        lEmp[0].append([])
        lEmp[1].append(list(lLignd))
        lEmp[2].append(list(lLigng))
    for y in range(0, m):
        lEmp[0][lD[y]].append([lA[y], lT[y]])

    # for dep in range(0,n):
    #	lEmp[1][dep][dep]=0
    #	lEmp[2][dep][dep]=True
    #	cherche(lEmp,dep)

    for r in range(0, r):
        if lEmp[2][ld[r]][la[r]]:
            print(lEmp[1][ld[r]][la[r]])
        else:
            dep = ld[r]
            lEmp[1][dep][dep] = 0
            lEmp[2][dep][dep] = True
            cherche(lEmp, dep)
            print(lEmp[1][ld[r]][la[r]])


if __name__ == '__main__':
    n, m, r = (int(i) for i in input().split())

    lD = []
    lA = []
    lT = []
    for _ in range(m):
        my_lD, my_lA, my_lT = (int(i) for i in input().split())
        lD.append(my_lD - 1)
        lA.append(my_lA - 1)
        lT.append(my_lT)

    ld = []
    la = []
    for _ in range(r):
        my_d, my_a = (int(i) for i in input().split())
        ld.append(my_d - 1)
        la.append(my_a - 1)

    expert_itinerant(n, m, r, lD, lA, lT, ld, la)
