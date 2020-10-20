expr = input('DIGITE SUA EXPRESSÃO: ')
pilha = 0

for simbolo in expr:
    if simbolo == '(':
        pilha += 1
    elif simbolo == ')':
        pilha += -1

    if pilha < 0:
        break

if pilha == 0:
    print('expressão correta')
elif pilha != 0:
    print('expressão incorreta')
