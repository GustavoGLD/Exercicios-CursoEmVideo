soma = 0

numeros = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')),
          int(input('Digite um número: ')))

print(f"Temos {numeros.count(9)} nove's")

if numeros.count(3) > 0:
    print(f'O primeiro numero três apareceu em {numeros.index(3)}')

for c in numeros:
    if c % 2 == 0:
        soma += 1

print(f'Temos {soma} números pares')