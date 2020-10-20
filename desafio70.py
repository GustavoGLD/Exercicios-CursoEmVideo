print('Exercício 70 – Estatísticas em produtos')

soma = 0
contagem = 0
deseja_continuar = 'khxhtxfd'
produto = produto_mais_caro = produto_mais_barato = input('Digite o produto: ')
preço_produto = preço_mais_caro = preço_mais_barato = float(input('Digite o preço: R$'))
deseja_continuar = input('Tem mais produtos para cadastras (s/n)? ')

while True:
    contagem += 1
    if contagem > 1:
        produto = input('Digite o produto: ')
        preço_produto = float(input('Digite o preço: R$'))
        deseja_continuar = input('Tem mais produtos para cadastras (s/n)? ')
        if preço_produto > preço_mais_caro:
            produto_mais_caro = produto

        if preço_produto < preço_mais_barato:
            produto_mais_barato = produto

    soma += preço_produto

    if deseja_continuar in 'nN':
        break

print(f'O mais caro foi o {produto_mais_caro} custando {preço_mais_caro}')
print(f'O mais barato {produto_mais_barato} custando {preço_mais_barato}')
print(f'No total, custou {soma}')
print(contagem)