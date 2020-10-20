# Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso,
# de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

cor = '\033[34m'
limpar = '\033[m'
tupla_numeros_extenso = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez'

print('Exercício 72 – Número por Extenso')

while True:
    while True:
        numero_pedido = int(input('ESCREVA UM NÚMERO DE 0 A 10 (-1 para sair): '))
        if -1 <= numero_pedido <= 10:
            break

    if numero_pedido == -1:
        break
    print(f'{cor}{numero_pedido}{limpar} por extenso é {cor}{tupla_numeros_extenso[numero_pedido]}{limpar}')

