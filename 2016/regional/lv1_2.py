def velociraptors(j, v, n):
    new = 0
    for x in range(0, n):
        new = j * 2 + v

        v = j
        j = new

    print(j + v)


(j, v) = list(map(int, input().split()))
n = int(input())
velociraptors(j, v, n)
