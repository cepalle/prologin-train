def les_bons_skis(nbSkis, taillePersonne, skis):
    diff_min = float('inf')
    ski_diff_min = skis[0]
    for ski in skis:
        if diff_min > abs(taillePersonne - ski):
            diff_min = abs(taillePersonne - ski)
            ski_diff_min = ski
        elif diff_min == abs(taillePersonne - ski) and ski < ski_diff_min:
            ski_diff_min = ski

    print(ski_diff_min)


nbSkis = int(input())
taillePersonne = int(input())
skis = list(map(int, input().split()))
les_bons_skis(nbSkis, taillePersonne, skis)
