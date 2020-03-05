n = int(input())
m = int(input())

for _ in range(0, n):
    l = [int(e) for e in input().split()]
    old = 0
    tot_cur = 0
    lres = []
    for e in l:
        if e == old:
            tot_cur += 1
        else:
            lres.append(tot_cur)
            tot_cur = 1
            old = e
    if tot_cur != 0:
        lres.append(tot_cur)

    for i in range(0, len(lres)):
        if i == 0:
            print(lres[i], end='')
        else:
            print(" " + str(lres[i]), end='')
    print()