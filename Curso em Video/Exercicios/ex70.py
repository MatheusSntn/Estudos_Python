total = totmil = menor = cont = 0  # total sera ele + o preco
barato = ''
while True:
    produto = input('nome do produto: ')
    preco = float(input('preco: R$'))
    cont += 1  # lendo a quantia de produto a partir daqui
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = input('Quer continuar? [S/N]').strip().upper()[0]
    if resp == 'N':
        break
print(':-^40'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${total:10.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000')
print(f'O produto mais barato foi {barato} que custa R${menor}')
