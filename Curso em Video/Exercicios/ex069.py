logo = 'CADASTRE UMA PESSOA'
print('=' * 30)
print(f'{logo: ^30}')
print('=' * 30)
maior_idade = cont_m = cont_f = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF'
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if sexo == 'M':
        cont_m += 1
    if idade > 18:
        maior_idade += 1
    if sexo == 'F' and idade < 20:
        cont_f += 1
    
    opcao = ' '
    
    while opcao not in 'SN':
        print('-' * 30)
        opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        print('-' * 30)
    if opcao == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {maior_idade}')
print(f'Ao  todo temos {cont_m} homens cadastrados.')
print(f'Ao temos temos {cont_f} mulheres com menos de 20 anos cadastradas.')

    