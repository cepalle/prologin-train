import heapq

l = int(input())
lt = [int(e) for e in input().split()]

memo = [float('inf') for _ in lt]

pile = [
    (0, 0)
]
memo[0] = 0
while len(pile) > 0:
    p, h = heapq.heappop(pile)
    p1 = (p + 1) % len(lt)
    p2 = (p - 1 + len(lt)) % len(lt)
    p3 = (p + lt[p]) % len(lt)
    if memo[p1] > h + 1:
        memo[p1] = h + 1
        heapq.heappush(pile, (p1, h + 1))
    if memo[p2] > h + 1:
        memo[p2] = h + 1
        heapq.heappush(pile, (p2, h + 1))
    if memo[p3] > h + 1:
        memo[p3] = h + 1
        heapq.heappush(pile, (p3, h + 1))

for i in range(0, len(memo)):
    if i != 0:
        print(" ", end="")
    print(memo[i], end="")
print()
