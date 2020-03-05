def censure0(n, st, m, positions):
    for i in range(0, len(st)):
        if (positions != [] and i == positions[0] - 1):
            for j in range(0, len(st[i])):
                print("*", end="")
            print(" ", end="")
            positions.pop(0)
        else:
            print(st[i], end=" ")
    print()


n = int(input())
st = list(map(str, input().split()))
m = int(input())
positions = list(map(int, input().split()))
censure0(n, st, m, positions)
