matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = 0
soma_3o_coluna = 0
for a in range(0, 3):
    for b in range(0, 3):
        matriz[a][b] = int(input(f'DIGITE O NÚMERO EM ({a + 1},{b + 1}): '))
for aa in range(0, 3):
    print(' ')
    for bb in range(0, 3):
        print([matriz[aa][bb]], end=' ')
        if matriz[aa][bb] % 2 == 0:
            pares += matriz[aa][bb]
        if bb == 2:
            soma_3o_coluna += matriz[aa][bb]
        if aa == 1 and bb == 0:
            maior = matriz[aa][bb]
        elif aa == 1 and bb == 1 and matriz[aa][bb] > maior:
            maior = matriz[aa][bb]
        elif aa == 1 and bb == 2 and matriz[aa][bb] > maior:
            maior = matriz[aa][bb]

print(f'\nA SOMA DOS NÚMEROS PARES RESULTAM EM {pares}')
print(f'A SOMA DA TERCEIRA COLUNA RESULTA EM {soma_3o_coluna}')
print(f'O MAIOR NÚMERO DA SEGUNDA LINHA É {maior}')
