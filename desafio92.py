dados = {'NOME':input('NOME: '),
         'DATA DE NASCIMENTO':int(input('ANO DE NASCIMENTO: ')),
         'NÚMERO DA CARTEIRA DE TRABALHO':int(input('CARTEIRA DE TRABALHO (0 SE NÃO TEM): '))}

if dados['NÚMERO DA CARTEIRA DE TRABALHO'] > 0:
    dados['ANO DE CONTRATAÇÃO'] = int(input('ANO DE CONTRATAÇÃO: '))
    dados['SALÁRIO'] = int(input('SALÁRIO: '))

for key, item in dados.items():
    print(f'{key} EQUIVALE A {item}')