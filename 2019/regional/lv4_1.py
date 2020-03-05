n = int(input())
m = int(input())
k = int(input())

memo = {}


def count_tour(n, m):
    if n == 0:
        return 1
    if m <= 0:
        return 0
    if n == 1:
        return m

    key = str(n) + " " + str(m)
    if key in memo:
        return memo[key]

    res = 0
    for nb in range(0, k + 1):
        if nb <= n:
            res += count_tour(n - nb, m - 1)
    memo[key] = res
    return res


print(count_tour(n, m))
