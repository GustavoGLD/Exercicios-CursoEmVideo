print('TABUADA')
n = int(input('escolha qual número você quer ver a tabuada: '))
q = int(input('De 0 até que número? '))

nt = 0
for c in range(0, q):
    nt = nt + 1
    print('{} * {} = {}'.format(n, nt, n * nt))

print('Espero ter te ajudado em matemática (ºuº)')