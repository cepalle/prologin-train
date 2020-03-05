n = int(input())
m = int(input())

lp = []
for _ in range(0, m):
    lp.append([int(e) for e in input().split()])


def check_posd(x, y, c):
    for p in lp:
        if (x <= p[0] <= x + c) and (y <= p[1] <= y + c):
            return False
    return True


mxc = 0
for y in range(0, n):
    for x in range(0, n):
        for c in range(0, n - max(y, x)):
            if check_posd(y, x, c):
                mxc = max(mxc, c)
            else:
                break

print(mxc + 1)