from random import randint
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = dict()
for key, value in jogo.items():
    print(f'O {key} tirou {value}')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for a, b in enumerate(ranking):
    print(f'O {a+1}º lugar foi o {b[0]} com {b[1]}')