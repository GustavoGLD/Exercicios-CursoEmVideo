print('Exercício 76 – Lista de Preços com Tupla'.upper())
produto = 'RAM 1GB', '15.00', 'RAM 2GB', '35.00', 'RAM 4GB', '75.00', 'RAM 8GB', '130.00'

for c in range(0, len(produto), 2):
    print(produto[c], '-' * 10, 'R$', produto[c + 1])