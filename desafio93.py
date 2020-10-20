dados = {'nome': input('NOME DO JOGADOR: ')}
gols_dicio = {}
total = 0
for contagem in range(0, int(input(f'QUANTAS PARTIDAS {dados["nome"]} JOGOU?'.upper()))):
    gols_dicio[f'{contagem + 1}'] = int(input(f'GOLS NA PARTIDA {contagem + 1}: '))
dados['gols'] = gols_dicio.values()
dados['total'] = sum(gols_dicio.values())
print('-=' * 40, '\n', dados, '\n', '-=' * 40)
for key, value in dados.items():
    print(f'O campo {key} tem o valor {value}')
print('-=' * 40)
print(f'O JOGADOR {dados["nome"]} MARCOU {dados["total"]} GOLS:')
for key, value in gols_dicio.items():
    print(f'NA {key}º JOGADA MARCOU {value} GOLS')