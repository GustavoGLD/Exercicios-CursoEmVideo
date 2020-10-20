# Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from time import sleep
from random import randint
jogada_pc = randint(0, 10)

cor = '\033[34m'
limpar = '\033[m'

print('>>' * 18)
print('Exercício 68 – Jogo do Par ou Ímpar')
print('>>' * 18)

vitorias_contagem = 0
derrotas_contagem = 0

while True:
    while True:
        jogada_player = int(input('ESCOLHA UM NÚMERO {}INTERIO{} DE 0 A 10: '.format(cor, limpar)))

        if 0 <= jogada_player <= 10:
            break
        else:
            print('SOMENTE NÚMEROS DE {}0{} A {}10{}!'.format(cor, limpar, cor, limpar))
            sleep(0.5)

    while True:
        escolha_impar_par = input('ESCOLHA APOSTAR NO {}ÍMPAR{} OU {}PAR{} (i/p): '.format(cor, limpar, cor, limpar))

        if escolha_impar_par in 'ipIP':
            break
        else:
            print('ESCREVA "{}i{}" PARA {}IMPAR{} OU "{}p{}" PARA {}PAR{}!'.format(cor, limpar, cor, limpar, cor, limpar, cor, limpar))
            sleep(0.5)

    print(f'COMPUTADOR JOGOU {jogada_pc}, QUE MAIS {jogada_player} FICAM  {jogada_pc + jogada_player}')
    if (jogada_player + jogada_pc) % 2 == 0:
        if escolha_impar_par in 'Pp':
            vitorias_contagem += 1
            print(f'{cor}VOCÊ ACERTOU!{limpar}')
        else:
            derrotas_contagem += 1
            print(f'{cor}VOCÊ ERROU!{limpar}')
    if (jogada_player + jogada_pc) % 2 == 1:
        if escolha_impar_par in 'Ii':
            vitorias_contagem += 1
            print(f'{cor}VOCÊ ACERTOU!{limpar}')
        else:
            derrotas_contagem += 1
            print(f'{cor}VOCÊ ERROU!{limpar}')

    if derrotas_contagem >= 3:
        print(f"\033[31m\nGAME OVER!{limpar}")
        sleep(0.5)
        print(f"VOCÊ GANHOU {vitorias_contagem} VEZES")
        break