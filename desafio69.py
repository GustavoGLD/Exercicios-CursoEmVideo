print('Exercício 69 – Análise de dados do grupo')
garotos = []
garotas = []
homens = []
mulheres = []

while True:
    nome = input('DIGITE O NOME: ')
    idade = int(input('DIGITE A IDADE: '))
    gênero = input('DIGITE O GÊNERO ("f"/"m"): ')

    if gênero in 'Ff':
        if idade >= 18:
            mulheres += [nome]
        else:
            garotas += [nome]

    if gênero in 'Mm':
        if idade >= 18:
            homens += [nome]
        else:
            garotos += [nome]

    resposta_continuação = input('DESEJA ADICIONAR MAIS PESSOAS A LISTA ("s"/"n")? ')

    if resposta_continuação in 'Nn':
        break

print(f"""{mulheres} são mulheres
{garotas} são garotas
{homens} são homens
{garotos} são garotos""")

