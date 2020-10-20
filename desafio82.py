lista_numeros = []
lista_pares = []
lista_impares = []

while True:
    n = int(input('DIGITE UM NÚMERO: '))
    lista_numeros.append(n)
    if n % 2 == 0:
        lista_pares.append(n)
    else:
        lista_impares.append(n)
    if input('DESEJA CONTINUAR (s/n): ') in 'nN':
        break

print(f'NÚMEROS: {lista_numeros}'
      f'\nNÚMEROS PARES: {lista_pares}'
      f'\nNÚMEROS ÍMPARES: {lista_impares}')