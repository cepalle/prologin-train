def course_baveuse0(n, c, joueur1, joueur2):
    while (1):
        if (joueur1 == []):
            print(n * 2 - len(joueur2) + 1)
            exit()
        if (joueur2 == []):
            print(n - len(joueur1) + 1)
            exit()
        if (joueur2[0]["vitesse"] == 0):
            joueur2.pop(0)
            continue
        if (joueur1[0]["vitesse"] == 0):
            joueur1.pop(0)
            continue
        if (float(joueur1[0]["position"]) / float(joueur2[0]["vitesse"]) < float(joueur2[0]["position"]) / float(
                joueur1[0]["vitesse"])):
            joueur1.pop(0)
        else:
            joueur2.pop(0)


(n, c) = list(map(int, input().split()))
joueur1 = [None] * n
for i in range(0, n):
    (p, v) = list(map(int, input().split()))
    joueur1[i] = {
        "position": p,
        "vitesse": v}
joueur2 = [None] * n
for i2 in range(0, n):
    (p2, v2) = list(map(int, input().split()))
    joueur2[i2] = {
        "position": p2,
        "vitesse": v2}
course_baveuse0(n, c, joueur1, joueur2)
