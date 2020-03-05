n = int(input())
tr = int(input())
ldl = [int(e) for e in input().split()]

lcur = []
lmax = 0

for i in range(0, len(ldl)):
    lcur.append(ldl[i])
    lcur.sort()
    while lcur[-1] - lcur[0] > tr:
        lcur.remove(ldl[i - len(lcur) + 1])
    lmax = max(lmax, len(lcur))

print(lmax - 1)