d_viagem = float(input('Qual a distancia da viagem em KM: '))
c_viagem = 0.50 * d_viagem
l_viagem = 0.45 * d_viagem

if d_viagem <= 200:
    print('Sua viagem custará R${}'.format(c_viagem))
else:
    print('Sua viagem custará R${}'.format(l_viagem))
