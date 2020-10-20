# Exercício Python 66: Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

while True:
    contagem = 1
    print('Exercício 66 – Vários números com flag')
    num = soma = float(input('DIGITE UM NÚMERO: '))
    while True:
        num = float(input('DIGITE UM OUTRO NÚMERO [999 PARA PARAR]: '))
        if num == 999:
            break
        soma += num
        contagem += 1
    print(f'VOCÊ DIGITOU {contagem} NÚMEROS. A SOMA EQUIVALE A {soma}')

    print("""DIGITE O NÚMERO DA AÇÃO QUE VOCÊ QUER TOMAR:
    DIGITE [1] PARA REPETIR O PROCESSO
    DIGITE [2] PARA SAIR""")
    resposta = input('>>')

    if resposta == "2":
        print('BYE BYE!')
        break
    if resposta not in "12":
        print('RECOMEÇANDO...')