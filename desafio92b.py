from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
dados['idade'] = - int(input('Ano de Nascimento: ')) + datetime.now().year
dados['ctps'] = int(input('Carteira de Trabalho (0 se não tiver): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = 35 - (datetime.now().year - dados['contratação'])
print('\n', '-=' * 20)
for key, value in dados.items():
    print(f'- {key} tem valor {value}')