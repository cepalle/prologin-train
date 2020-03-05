tab = []


def cal_rec(recette, i):
    if (tab[i] != -1):
        return tab[i]
    res = 0
    for rec in recette[i]:
        res = max(res, rec[1] + cal_rec(recette, rec[0]))
    tab[i] = res
    # print(i, res)
    return res


def cuisine(recette):
    # print(recette)
    for i in range(0, len(recette)):
        tab.append(-1)

    for i in range(0, len(recette)):
        cal_rec(recette, i)
    # print(tab)
    return max(tab)


if __name__ == "__main__":
    n = int(input())

    recette = []
    for _ in range(n):
        l = list(map(int, input().split()))
        recette.append([(l[2 * j + 1], l[2 * j + 2]) for j in range(l[0])])

    print(cuisine(recette))
