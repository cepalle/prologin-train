n, m = [int(e) for e in input().split()]
M = [list(input()) for _ in range(0, n)]

dd = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
]

pile = [
    (0, 0)
]
M[0][0] = '-'
while len(pile) > 0:
    x, y = pile.pop(0)
    for d in dd:
        nx = x + d[0]
        ny = y + d[1]
        if 0 <= ny < n and 0 <= nx < m:
            if M[ny][nx] == '.':
                M[ny][nx] = '-'
                pile.append((nx, ny))

tot = 0
for l in M:
    for e in l:
        if e == '.':
            tot += 1

print(tot)
