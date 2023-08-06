caminho = 'testedowith'

with open(caminho, 'r+') as arquivo:
    arquivo.write('AAAAAAAAAAA\n')
    arquivo.write('AAAAAAAAAAA')
    arquivo.writelines(
        ('Writeline podemos escrever\n', 'neste formato\n', 'Em tuplas')
    )
    print(arquivo.read())
    print('lendo')
    arquivo.seek(0, 0)
    # readline = le como se fosse um next
    # precisarei de mais linhas de readline em baixo
    # caso quisesse ler mais do arquivo
    print(arquivo.readline()) 
    print('READLINES')
    arquivo.seek(0,0)
    for linha in arquivo.readlines():
        print(linha.strip())
print('-' * 20)

with open(caminho, 'r') as arquivo:
    print(arquivo.read())

