r1 = float(input('primeiro segmento: '))
r2 = float(input('primeiro segmento: '))
r3 = float(input('primeiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É possível formar um triangulo')
    if r1 == r2 and r2 == r3:
        print('Todos os lados são iguais. Triangulo Equilátero.')
    elif r1 == r2 or r2 == r3:
        print('Dois lados são iguais. Triangulo Isósceles.')
    elif r1 != r2 and r2 != r3:
        print('Todos os lados sao diferentes.Triangulo Escaleno')
else:
    print('Não será possível formar um triangulo')
