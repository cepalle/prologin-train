#!/usr/bin/env python3
if __name__ == '__main__':
    un, k = int(input()), int(input())
    for op in range(0, k):
        if un % 2 == 0:
            un = int(un / 2)
        else:
            un = 3 * un + 1
    print(un)
