totgasto = mais_mil = mais_barato = cont = 0
barato = ''
while True:
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preco do produto: '))
    cont += 1
    opcao = ' '
    totgasto += preco
    nome_barato = nome 
    if preco >= 1000:
        mais_mil += 1
    if cont == 1 or preco < mais_barato:
        mais_barato = preco
        barato = nome
    while opcao not in 'SN':
        opcao = str(input('Existe mais algum produto? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break 

print(f'Total de gasto: {totgasto}')
print(f'Total de produtos que custam mais de R$1000,00: {mais_mil}')
print(f'Nome do produto mais barato: {barato}')
