tot18 = totH = totM20 = 0

while True:
    nome = ' '
    idade = ' '
    sexo = ' '

    print("-" * 40)
    print("CADASTRE UMA PESSOA")
    print("-" * 40)
    nome = input('Nome:')
    idade = int(input('idade:'))
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1

    resp = ' '
    while resp not in 'SN':
        print('-' * 30)
        resp = str(input('GOSTARIA DE CONTINUAR? [S/N]')).strip().upper()[0]
        print('-' * 30)
    if resp == 'N':
        break
print('acabou')
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} homens cadastrados')
print(f'E temos {totM20} mulheres com menos de 20 anos')
