n, s, t = [int(e) for e in input().split()]
s -= 1
t -= 1
if s > t:
    tmp = s
    s = t
    t = tmp

s1 = 0
s2 = 0
for i in range(0, n):
    if s <= i < t:
        s1 += int(input())
    else:
        s2 += int(input())

print(min(s1, s2))
