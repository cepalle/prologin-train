input()
lt = [int(e) for e in input().split()]
input()
i = list(input())

pos = 0
for e in i:
    if e == "A":
        pos += 1
    elif e == "R":
        pos -= 1
    else:
        pos += lt[pos]

    pos += len(lt)
    pos %= len(lt)
print(pos + 1)
