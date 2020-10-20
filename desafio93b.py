partidas = list()
jogador = {'nome': input('QUAL O NOME DO JOGADOR? ')}
for c in range(0, int(input(f'QUANTAS PARTIDAS {jogador["nome"].upper()} JOGOU? '))):
    partidas.append(int(input(f'QUANTOS GOLS {jogador["nome"].upper()} JOGOU NA {c + 1}º PARTIDA? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 40, '\n', jogador, '\n', '-=' * 40)
for key, value in jogador.items():
    print(f'O CAMPO {key} TEM VALOR {value}'.upper())
print('-=' * 40, '\n', f'O JOGADOR {jogador["nome"]} TEVE {len(jogador["gols"])}: ')
for c, value in enumerate(jogador["gols"]):
    print(f'NA {c + 1}º PARTIDA MARCOU {value} GOLS')