p = float(input())
q = float(input())
n = int(input())

res = 0
for _ in range(0, n):
    pp, qq = [float(e) for e in input().split()]
    if (q / p) <= (qq / pp):
        res += 1
print(res)
