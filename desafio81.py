lista = []
while True:
    lista.append(int(input('DIGITE UM NÚMERO: ')))
    if input('DESEJA CONTINUAR? (S/N)') in 'nN':
        break

print(f'\nVOCÊ DIGITOU {len(lista)} NÚMEROS')
print('Os números digitados:', lista)
if 5 in lista:
    print('O 5 ESTÁ NA LISTA, NAS POSIÇÕES ', end='')
    for a, b in enumerate(lista):
        if lista[a] == 5:
            print(a + 1, end=' ')
else:
    print('NÃO TEM 5')
lista.sort(reverse=True)
print('\nOs números digitados, em ordem decrescente:', lista)
