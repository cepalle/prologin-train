n = int(input())
m = int(input())
lj = [int(e) for e in input().split()]
lj.sort()
la = [int(e) for e in input().split()]
la.sort()

while len(lj) > 0 and len(la) > 0:
    if la[0] <= lj[0]:
        lj.pop(0)
        la.pop(0)
        continue
    la.pop(0)

if len(lj) != 0:
    print("Il faut planter plus d'arbres !")
else:
    print("Miam !")