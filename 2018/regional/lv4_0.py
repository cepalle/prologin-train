n, t, x, k = [int(e) for e in input().split()]
lt = [int(e) for e in input().split()]
lt.sort()


def main():
    allPoss = set()
    allPoss.add(0)
    for _ in range(0, k + 2):
        old = set(allPoss)
        for r in old:
            if t - x <= r <= t + x:
                print('OUI')
                return
            for e in lt:
                allPoss.add(r + e)
                allPoss.add(r - e)

    print('NON')


main()
