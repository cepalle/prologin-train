def paravent(n, hauteurs):
    tot = 0
    mx = 0
    for h in hauteurs:
        if (h < mx):
            tot += 1
        else:
            mx = h
    print(tot)


n = int(input())
hauteurs = list(map(int, input().split()))
paravent(n, hauteurs)
