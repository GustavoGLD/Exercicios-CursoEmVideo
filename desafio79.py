numeros_lista = []

while True:
    resposta = input('DESEJA CONTINUAR (s/n)? ')
    if resposta in 'nN':
        break

    else:
        numero_dado = int(input('DIGITE UM NÚMERO INTEIRO: '))
        if numero_dado not in numeros_lista:
            numeros_lista.append(numero_dado)
            print('NÚMERO ADICIONADO COM SUCESSO!')
        else:
            print('NÚMERO JÁ ESCRITO, NÃO VOU ADICIONAR!')

print(numeros_lista)