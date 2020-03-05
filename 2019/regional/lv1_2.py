tot = 0
for _ in range(0, 5):
    l = input()
    for e in l:
        if e == 'X':
            tot += 1

if tot < n:
    tot = -1
print(tot)