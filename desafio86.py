lista1 = []
lista2 = []
lista3 = []
for c in range(1, 10):
    if c <= 3:
        lista1.append([int(input(f'DIGITE O NÚMERO EM (1, {c}): '))])
    elif c <= 6:
        lista2.append([int(input(f'DIGITE O NÚMERO EM (2, {c - 3}): '))])
    elif c <= 9:
        lista3.append([int(input(f'DIGITE O NÚMERO EM (3, {c - 6}): '))])
print(f'{lista1} \n{lista2} \n{lista3}')