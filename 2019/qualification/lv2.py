n = int(input())
ldh = [[int(e) for e in input().split()] for _ in range(0, n)]
v = int(input())
ldp = [[int(e) for e in input().split()] for _ in range(0, v)]

p1 = 0
p2 = 0
for e in ldp:
    if e[0] == 1:
        p1 = ldh[e[1] - 1][1]
    else:
        p2 = ldh[e[1] - 1][1]
    print(abs(p1 - p2))
