# Exercício Python 67: Faça um programa que mostre a tabuada de vários números,
# um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

from time import sleep

while True:
    print('Exercício 67 – Tabuada v3.0')
    n = int(input('QUAL TABUADA VOCÊ QUER VER: '))
    q = int(input('TABELA DE 0 ATÉ QUE NÚMERO? '))
    s = 1

    while True:
        if s > q:
            break
        print(f'{n}x{s}={n * s}')
        s += 1

    sleep(1)

    while True:
        print("""SELECIONE QUAL TOMADA VOCÊ QUER LIDAR:
DIGITE [1] PARA VER OUTRA TABOADA
DIGITE [2] PARA SAIR""")
        resp = input('>>')

        if resp in "12":
            break
        else:
            print('POR FAVOR, PRESTE ATENÇÃO NAS ORIENTAÇÕES!')
    if resp == '2':
        break