def frise_chronologique(d, n, frise):
    tot = 1
    for date in frise:
        if (date < d):
            tot += 1
    print(tot)


d = int(input())
n = int(input())
frise = list(map(int, input().split()))
frise_chronologique(d, n, frise)
