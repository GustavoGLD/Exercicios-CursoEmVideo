aluno = {'nome':input('NOME: '), 'média':input('MÉDIA: ')}
for key, value in aluno.items():
    print(f'{key} é igual a {value}\n', 'Situação é igual a ','Reprovado' if aluno["Média"] < 7 else "Aprovado"'')