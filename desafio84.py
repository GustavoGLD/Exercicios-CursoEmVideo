temp = []
princ = []
maior = menor = 0

while True:
    temp.append(input('NOME: '))
    temp.append(float(input('PESO: ')))

    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]

    princ.append(temp[:])
    temp.clear()

    if input('CONTINUAR? [S/N]: ') in 'nN':
        break

print(f'VOCÊ CADASTROU {len(princ)} PESSOAS')
print(f'\nO MAIOR PESO FOI DE {maior}Kg DE ', end='')

for c in princ:
    if c[1] == maior:
        print(c[0], end=' ')

print(f'\nO MENOR PESO FOI DE {menor}Kg DE ', end='')

for c in princ:
    if c[1] == menor:
        print(c[0], end=' ')
