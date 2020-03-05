def is_out(pos, n):
    return pos[0] < 0 or pos[1] < 0 or pos[0] >= n or pos[1] >= n


def courants_marins(n, courants):
    pos = [int(n / 2), int(n / 2)]
    tot = 0
    while 1:
        if (is_out(pos, n)):
            print(tot)
            return

        sym = courants[pos[0]][pos[1]]
        if (sym == ">"):
            courants[pos[0]][pos[1]] = "o"
            pos[1] += 1
        elif (sym == "<"):
            courants[pos[0]][pos[1]] = "o"
            pos[1] -= 1
        elif (sym == "^"):
            courants[pos[0]][pos[1]] = "o"
            pos[0] -= 1
        elif (sym == "v"):
            courants[pos[0]][pos[1]] = "o"
            pos[0] += 1
        else:
            print(0)
            return
        tot += 1


n = int(input())
courants = [list(input()) for _ in range(n)]
courants_marins(n, courants)
