nome = input('Digite seu nome: ').strip()
print('Analisando seu nome...')
print('Seu nome em maiusculo é ' + nome.upper())
print('Seu nome em minusculo é ' + nome.lower())
print('Seu nome tem ao todo ', len(nome) - nome.count(' '), 'letras')
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('seu primeiro nome é {} e ele tem {} letras'.format(
    separa[0], len(separa[0])))
