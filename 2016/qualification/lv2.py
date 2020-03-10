h = int(input())
input()
lh = [int(e) for e in input().split()]
tot = 0
for e in lh:
    if e < h:
        tot += h - e
print(tot)
