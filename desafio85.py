pares = []
impares = []
for c in range(1, 8):
    n = int(input(f'DIGITE O {c}º número: '))
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

pares.sort()
impares.sort()
print(f'OS PARES FORAM {pares}'
      f'\nOS ÍMPARES FORAM {impares}')
