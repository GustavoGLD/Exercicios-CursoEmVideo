principal = []
while True:
    principal.append([input('DIGITE O NOME: '), float(input('DIGITE A NOTA 1: ')), float(input('DIGITE A NOTA 2: '))])
    if input('QUE CONTINUAR (S/N)? ') in 'nN':
        break
for numero, aluno in enumerate(principal):
    print(f'{numero + 1}º) {aluno[0]:=<30} MÉDIA {(aluno[1] + aluno[2]) / 2}')
while True:
    resp = int(input('\nDIGITE O ALUNO QUEIRA VER MAIS INFORMAÇÕES (999 PARA): '))
    if resp <= len(principal):
        print(f'{principal[resp - 1][0]}: {principal[resp - 1][1]} na 1º atividade e {principal[resp - 1][2]} na 2º')
    if resp == 999:
        break