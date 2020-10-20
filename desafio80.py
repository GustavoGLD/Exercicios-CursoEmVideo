lista = []

for c in range(0, 5):
    n = int(input('DIGITE UM NÚMERO: '))

    if c == 0:
        maior = menor = n
        lista.append(n)
        print('NÚMERO ADICIONADO COM SUCESSO')
        print(lista)
    elif n > maior:
        maior = n
        lista.append(n)
        print('NÚMERO ADICIONADO AO FINAL DA LISTA')
        print(lista)
    elif n < menor:
        menor = n
        lista.insert(0,n)
        print('NÚMERO ADICIONADO AO INÍCIO DA LISTA')
        print(lista)
    else:
        for c in range(0, len(lista)):
            if n < lista[c]:
                lista.insert(c, n)
                print('NÚMERO ADICIONADO COM SUCESSO')
                print(lista)
                break
