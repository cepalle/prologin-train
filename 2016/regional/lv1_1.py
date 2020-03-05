def convert(x):
    v = 0
    if (x == "B"):
        v = 1
    elif (x == "C"):
        v = 2
    return v


def trois_dinosaures(x, y):
    if (x == y):
        print(0)
        return
    v1 = convert(x)
    v2 = convert(y)
    if ((v1 + 1) % 3 == v2):
        print(1)
        return
    print(2)


x = input().strip()
y = input().strip()
trois_dinosaures(x, y)
