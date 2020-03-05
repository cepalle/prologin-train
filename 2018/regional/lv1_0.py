n = int(input())


def consequ(w):
    tot = 0
    old = w[0]
    mx = 0
    for c in w:
        if old == c:
            tot += 1
        else:
            old = c
            tot = 1
        mx = max(mx, tot)
    return mx


for _ in range(0, n):
    l = int(input())
    w = input()
    if ord('A') <= ord(w[0]) <= ord('Z') and 5 <= l <= 15 and consequ(w) <= 2:
        print(w)
