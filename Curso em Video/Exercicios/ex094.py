geral = list()
cadastro = dict()
soma = tot = 0
mulheres_cadastradas = list()

while True:
    cadastro['nome'] = str(input('nome:'))
    cadastro['sexo'] = str(input('sexo [M/F]:' ))
    while cadastro['sexo'] not in 'MFmf':
        print('ERRO! Digite M ou F.')
        cadastro['sexo'] = str(input('sexo [M/F]: '))
    if cadastro['sexo'] in 'Ff':
        mulheres_cadastradas.append(cadastro['nome'])
    cadastro['idade'] = int(input('idade: '))
    soma += cadastro['idade']
    geral.append(cadastro.copy())
    tot += 1

    opcao = str(input('Quer continuar [S/N]:'))
    if opcao == 'n':
        break

print(f'Ao todo tem {tot} pessoas cadastradas.')

media = soma / tot

print(f'A media de idade é de {media} anos.')
print(f'As mulheres cadastradas foram {mulheres_cadastradas}.')

for c in geral:
    if c['idade'] >= media:
        print('   ')
        for k, v in c.items():
            print(f'{k} = {v}; ', end='')
        print()


