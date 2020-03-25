input()
lt = [int(e) for e in input().split()]


def main():
    for i in range(0, len(lt) - 1):
        if lt[i] - lt[i + 1] >= 2:
            print(0)
            return
    if lt[-1] - lt[0] >= 2:
        print(0)
        return
    print(1)


main()
