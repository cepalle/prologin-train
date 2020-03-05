def allocation_de_verrerie(n, formule):
    nb_pod = []
    for i in range(0, n):
        nb_pod_0 = 0
        nb_pod_1 = 0
        if (formule[i][0] >= 0):
            nb_pod_0 = nb_pod[formule[i][0]]
        if (formule[i][1] >= 0):
            nb_pod_1 = nb_pod[formule[i][1]]

        if (nb_pod_0 == nb_pod_1):
            nb_pod.append(nb_pod_0 + 1)
        else:
            nb_pod.append(max(nb_pod_0, nb_pod_1))

    print(nb_pod[-1])
    """Inserez votre code ici"""


n = int(input())
formule = [list(map(int, input().split())) for i in range(n)]
allocation_de_verrerie(n, formule)
