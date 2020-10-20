n0 = int(input('Digite o número inicial: '))
nf = int(input('Digite p número final: '))
m = int(input('Escolha o multiplo: '))

soma = 0
for c in range(n0, nf + 1):
    if c % m == 0:
        soma = soma + c
        print(c, end=', ')

print('\nA soma dos números multiplos de {} entre {} e {} é {}'.format(m, n0, nf, soma))