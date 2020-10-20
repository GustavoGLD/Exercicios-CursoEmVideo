soma = 0
n0 = int(input('Digite o número inicial: '))
nf = int(input('Digite p número final: '))
m = int(input('Escolha o multiplo: '))

if n0 % m != 0:
    while (n0 % m != 0):
        n0 = n0 + 1

for c in range(n0, nf + 1, m):
    soma = soma + c
    print(c, end=', ')

print('\nA soma dos números multiplos de {} entre {} e {} é {}'.format(m, n0, nf, soma))