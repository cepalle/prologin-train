def choix_des_skis(nbPersonnes, personnes, skis):
    personnes.sort()
    skis.sort()
    tot = 0
    for i in range(nbPersonnes):
        tot += abs(personnes[i] - skis[i])
    print(tot)


nbPersonnes = int(input())
personnes = list(map(int, input().split()))
skis = list(map(int, input().split()))
choix_des_skis(nbPersonnes, personnes, skis)
