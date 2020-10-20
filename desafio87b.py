matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = maior = soma_coluna = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'DIGITE O NA POSIÇÃO ({l}, {c}): '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'{matriz[l][c]}', end='')
        if matriz[l][c] % 2 == 0:
            soma_pares += matriz[l][c]
print(f'A SOMA DOS NÚMEROS PARES RESULTA EM {soma_pares}')
for l in range(0, 3):
    soma_coluna += matriz[l][2]
