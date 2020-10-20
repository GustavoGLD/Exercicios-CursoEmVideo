lista = []
dicio = {}
média = contador = 0
while True:
    dicio['nome'] = input('NOME: ')
    while True:
        dicio['gênero'] = input('GÊNERO(f/m): ')
        if dicio['gênero'] in 'fFmM':
            break
    dicio['idade'] = int(input('IDADE: '))
    lista.append(dicio)
    média += lista[-1]['idade'] / 2
    while True:
        resp = input('DESEJA CONTINUAR? (s/n): ')
        if resp in 'nNsS':
            break
    if resp in 'nN':
        break
    contador += 1
print(f'FORAM CADASTRADAS {len(lista)} PESSOAS'
      f'\nA MÉDIA DAS IDADES É DE {média} ANOS')
print(lista)
print(lista[0]['idade'])
for item in range(0, len(lista)):
    if lista[item]['idade'] > média:
        print(lista[item])
print('\n\n', lista)