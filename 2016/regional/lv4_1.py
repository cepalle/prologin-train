import heapq

k = int(input())
n = int(input())
ch = input()

for _ in range(0, k + 1):
    ch += ".."

dp = [float('inf') for _ in range(0, len(ch))]


def bfs():
    pile = [
        (0, 0)
    ]
    dp[0] = 0
    while len(pile) > 0:
        h, p = heapq.heappop(pile)
        if p >= n:
            return h
        if ch[p + 1] != "#" and h < dp[p + 1]:
            heapq.heappush(pile, (h, p + 1))
            dp[p + 1] = h
        if "^" not in ch[p + 1:p + k + 1] and ch[p + k] != "#" and h + 1 < dp[p + k]:
            heapq.heappush(pile, (h + 1, p + k))
            dp[p + k] = h + 1


r = bfs()
if r is None:
    print(-1)
else:
    print(r)
