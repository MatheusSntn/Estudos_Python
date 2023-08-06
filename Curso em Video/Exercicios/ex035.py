r1 = float(input('primeiro segmento: '))
r2 = float(input('primeiro segmento: '))
r3 = float(input('primeiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É possível formar um triangulo')
else:
    print('Não será possível formar um triangulo')
