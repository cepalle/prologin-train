from random import randint


def is_good(t, bn):
    for i in range(0, bn[1]):
        if (int(bn[0] / (2 ** (bn[1] - i - 1))) % 2 and
                t[i] < bn[1] and
                int(bn[0] / (2 ** (bn[1] - t[i] - 1))) % 2
        ):
            return False
    return True


def cal_bn(bn):
    sum = 0
    while (bn[0]):
        if (bn[0] % 2):
            sum += 1
        bn[0] = int(bn[0] / 2)
    return sum


def arche_minus0_aux(n, t):
    l_bn = [[0, 1], [1, 1]]
    mx = 0
    for bn in l_bn:
        if (bn[1] == n):
            mx = max(mx, cal_bn(bn))
        else:
            l_bn.append([bn[0] * 2, bn[1] + 1])
            if (is_good(t, [bn[0] * 2 + 1, bn[1] + 1])):
                l_bn.append([bn[0] * 2 + 1, bn[1] + 1])

    return mx


# -----------------------------

def prt(tab):
    for l in tab:
        for elt in l:
            print(elt, end="")
            print(" ", end="")
        print()


def rm_i(M, i):
    M.pop(i)
    for l in M:
        l.pop(i)


def arche_minus0(n, t):
    l = [0] * n
    M = []
    for i in range(0, n):
        M.append(list(l))
    for i in range(0, n):
        M[t[i]][i] = 1
        M[i][t[i]] = 1

    sup_1 = True
    sup_2 = True
    while (sup_1 or sup_2):
        # prt(M)
        # print()
        sup_1 = False
        sup_2 = False
        for i in range(0, len(M)):
            if (sum(M[i]) == 1):
                sup_1 = True
                for j in range(0, len(M[i])):
                    if (M[i][j]):
                        rm_i(M, j)
                        break
                break

        if (not sup_1):
            for i in range(0, len(M)):
                if (sum(M[i]) == 2):
                    sup_2 = True
                    rm_i(M, i)
                    break

    return len(M)


n = int(input())
t = list(map(int, input().split()))

# n = 20
# t = []
# for i in range(0, n):
#    t.append(randint(0, n - 1))

# print(n, t)
# print()


print("%d\n" % (arche_minus0(n, t)), end='')
# print("%d\n" % ( arche_minus0_aux(n, t) ), end='')
