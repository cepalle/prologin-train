n = int(input())
k = int(input())
lt = [int(e) for e in input().split()]

memo = {}


def sub_count(i, l):
    if l == 1:
        return 1
    key = str(i) + " " + str(l)
    if key in memo:
        return memo[key]
    res = 0
    for j in range(0, i):
        if lt[j] >= lt[i]:
            res += sub_count(j, l - 1)
    memo[key] = res
    return res


res = 0
for i in range(0, len(lt)):
    res += sub_count(i, k)

print(res)