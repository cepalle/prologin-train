input()
msg = list(input())

res = ""
while len(msg) > 0:
    cur = msg.pop(0)
    if cur == '.':
        continue
    if cur != '*':
        res += cur
        continue
    while len(msg) > 0:
        tmp = msg.pop(0)
        if tmp == '*':
            break

print(res)
