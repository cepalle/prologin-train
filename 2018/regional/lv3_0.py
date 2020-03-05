n, m = [int(e) for e in input().split()]
t = int(input())
ld = [[int(e) for e in input().split()] for _ in range(0, t)]


def dst(p1, p2):
    return max(abs(p1[0] - p2[0]), abs(p1[1] - p2[1]))


mxt = 0
for y in range(0, m):
    for x in range(0, n):
        tot = 0
        for e in ld:
            tot += max(0, e[2] - dst([x, y, 0], e))
        mxt = max(mxt, tot)
print(mxt)
