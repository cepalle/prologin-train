def pluie_de_meteorites(n, x, y, impacts):
    pos = [x, y]
    hys = []
    tour = 0

    for met in impacts:
        if (pos[0] == met[0] and pos[1] == met[1]):
            print(tour)
            return

        for i in range(0, 2):
            if (pos[i] < met[i]):
                pos[i] -= 1
            elif (pos[i] > met[i]):
                pos[i] += 1

        hys.append(met)
        for meth in hys:
            if (pos[0] == meth[0] and pos[1] == meth[1]):
                print(tour)
                return

        tour += 1

    print(tour)


n = int(input())
(x, y) = list(map(int, input().split()))
impacts = [list(map(int, input().split())) for i in range(n)]
pluie_de_meteorites(n, x, y, impacts)
