from random import randint

numeros = (randint(0, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os números sorteados foram {}'.format(numeros))
print(f'O maior número sorteado foi {max(numeros)} e o menor {min(numeros)}')