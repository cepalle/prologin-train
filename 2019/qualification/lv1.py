p = int(input())
input()
lp = [int(e) for e in input().split()]

if len(list(filter(lambda e: e < p, lp))) >= 3:
    print('ARNAQUE !')
else:
    print('Ok bon voyage, bisous, n\'oublie pas de m\'envoyer des photos !')
