n = int(input())
lf = [int(e) for e in input().split()]
lc = [int(e) for e in input().split()]

res = float('inf')
for i in range(0, n):
    res = min(lf[i] // lc[i], res)
print(res)
