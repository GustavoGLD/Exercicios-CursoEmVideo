from random import sample
for c in range(0, int(input('QUANTOS SORTEAMENTOS? '))):
    print(sample(range(1, 60), k=6))
