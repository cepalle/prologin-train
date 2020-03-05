#!/usr/bin/env python3
from cmath import *


def rondpoint(x, y, n, sorties):
    posR = complex(x, y)
    lPos = []
    for nb in range(0, n):
        lPos.append(complex(sorties[nb][0], sorties[nb][1]) - posR)

    posV, argV = lPos[0], phase(lPos[0])
    xMin, argMin = 1, (phase(lPos[1]) - argV) % (2 * pi)
    for x in range(2, len(lPos)):
        if min(argMin, (phase(lPos[x]) - argV) % (2 * pi)) != argMin:
            xMin = x
            argMin = (phase(lPos[xMin]) - argV) % (2 * pi)

    posSorti = lPos[xMin] + posR

    return int(posSorti.real), int(posSorti.imag)


if __name__ == "__main__":
    x, y = tuple(map(int, input().split()))
    n = int(input())
    sorties = [tuple(map(int, input().split())) for _ in range(n)]
    print("%d %d" % rondpoint(x, y, n, sorties))
