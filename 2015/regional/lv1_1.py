def deltaEncoding(n, tab):
    old = 0
    for elt in tab:
        print(elt - old, end="")
        old = elt
    print()


n = int(input())
tab = list(map(int, input().split()))
deltaEncoding(n, tab)
