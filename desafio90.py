aluno = dict()
aluno['nome'] = input('NOME: ')
aluno['média'] = float(input('MÉDIA: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'APROVADO'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'RECUPERAÇÃO'
else:
    aluno['situação'] = 'REPROVADO'
for key, value in aluno.items():
    print(f'{key} É IGUAL A {value}'.lower())