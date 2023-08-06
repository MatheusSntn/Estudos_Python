velocidade = float(input('Digite a velocidade atual do carro: '))
cont = 80
multa = (velocidade - 80) * 7
if velocidade > cont:
    print('Multado. Sua multa ira custar R${:.2f}'.format(multa))
else:
    print('parabens, continue assim.')
