from random import choice
sorteados = []
for c in range(0, int(input('QUANTOS SORTEIO? '))):
    numeros_possíveis = range(1, 61)
    for t in range(0, 6):
        sorteados.append(choice(numeros_possíveis))
    print(sorteados)
    sorteados.clear()