def crabe_americain(m, n, sol_marin):
    x = 0
    y = 0
    x_cr = 0
    y_cr = 0
    x_ch = 0
    y_ch = 0

    for ligne in sol_marin:
        x += 1
        y = 0
        for sol in ligne:
            y += 1
            if (sol == "$"):
                x_ch = x
                y_ch = y
            if (sol == "{"):
                x_cr = x
                y_cr = y
    print(abs(x_cr - x_ch) + abs(y_cr - y_ch))


(m, n) = list(map(int, input().split()))
sol_marin = [list(input()) for _ in range(m)]
crabe_americain(m, n, sol_marin)
