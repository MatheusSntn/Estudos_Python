produto = float(input('Digite o valor do produto: R$'))
pag_dinheiro = produto - (produto * 10/100)
pag_1xcartao = produto - (produto * 5/100)
pag_2xcartao = produto
pag_3xcartao = produto + (produto * 20/100)

print('-=-' * 15)
print(' ' * 15 + 'Lojas Matheus')
print('-=-' * 15)

print('''[ 1 ] A vista
[ 2 ] 1x No Cartão
[ 3 ] 2x No Cartão
[ 4 ] 3x'ou mais No Cartão''')

opcao = int(input('\nDigite uma opcao de pagamento: '))
if opcao == 1:
    print(f'Sua compra de R${produto} custará R${pag_dinheiro:.2f}.')
elif opcao == 2:
    print(f'Sua compra de R${produto} custará R${pag_1xcartao:.2f}.')
elif opcao == 3:
    print(f'Sua compra de R${produto} custará R${pag_2xcartao:.2}.')
elif opcao == 4:
    parcelas = int(input('Quantas parcelas?'))
    parcelas_mensais = pag_3xcartao / parcelas
    print(
        f'Sua compra será parcelada em {parcelas}x de R${parcelas_mensais:.2f} COM JUROS.')
    print(f'Sua compra de {produto} custará R${pag_3xcartao}.')
