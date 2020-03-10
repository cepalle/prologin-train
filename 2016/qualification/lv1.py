h = int(input())
input()
lh = [int(e) for e in input().split()]
print(1 if min(lh) < h else 0)
