def creneaux0(n, h):
    print(" _ ", end="")
    for i in range(0, n - 1):
        print("  _ ", end="")
    print()

    print("| |", end="")
    for i in range(0, n - 1):
        print("_| |", end="")
    print()

    for j in range(0, h - 2):
        print("|  ", end="")
        for i in range(0, n - 2):
            print("    ", end="")
        print("   |")

    print("|__", end="")
    for i in range(0, n - 2):
        print("____", end="")
    print("___|")


n = int(input())
h = int(input())
creneaux0(n, h)
