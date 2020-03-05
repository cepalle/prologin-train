n = int(input())


def check(n3, n2, n1):
    n = n3 * 100 + n2 * 10 + n1
    if n == 0:
        return False
    if n % 2 == 0 or n % 5 == 0 or n % 11 == 0:
        return False
    if (n3 + n2 + n1) % 2 == 0:
        return False
    if (n3 * n2 * n1) % 2 == 1:
        return False
    return True


for n3 in range(0, n + 1):
    for n2 in range(0, n + 1):
        for n1 in range(0, n + 1):
            if check(n3, n2, n1):
                print(str(n3) + str(n2) + str(n1))
