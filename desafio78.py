numeros = []
posições_maior = []
posições_menor = []

for c in range(0, 5):
    numeros.append(int(input('Escreva um número: ')))

maior = menor = numeros[0]
for posição, numero in enumerate(numeros):
    if numero > maior and posição != 0:
        posições_maior = []
        maior = numero
        posições_maior.append(posição + 1)
    elif numero == maior:
        posições_maior.append(posição + 1)

    if numero < menor and posição != 0:
        posições_menor = []
        menor = numero
        posições_menor.append(posição + 1)
    elif numero == menor:
        posições_menor.append(posição + 1)

print(f' O maior número foi {maior} e apareceu nas posições ', end='')
for t, c in enumerate(posições_maior):
    if t == len(posições_maior) - 1:
        print(c)
    if t != len(posições_maior) - 1:
        print(c, end=', ')


print(f'\n O menor número foi {menor} e apareceu nas posições {posições_menor}')