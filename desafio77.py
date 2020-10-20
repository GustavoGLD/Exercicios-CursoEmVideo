palavras = ('inentendivel', 'compreender', 'obrigaçoes', 'serem', 'escritas')

for c in range(0, len(palavras)):
    print('\n', palavras[c], end=' ')
    for l in palavras[c]:
        if l in 'aeiouAEIOU':
            print(l, end=', ')