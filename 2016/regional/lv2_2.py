def stonehenge(n, plan):
    l = 0
    for elt in plan:
        l += 1
    tot = 0
    for i in range(1, l):
        if (plan[i] != plan[l - i]):
            tot += 1
    print(tot)


n = int(input())
plan = list(input())
stonehenge(n, plan)
