from random import randint
for l in range(0, int(input('QUANTOS QUER QUE EU SORTEIE? '))):
    lista = [0, 0, 0, 0, 0, 0]
    for c in range(0, 6):
        n = randint(1, 60)
        while lista.count(n) > 0:
            n = randint(1, 60)
        lista[c] = n
    print(lista)