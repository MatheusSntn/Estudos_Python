n = int(input('digite um numero para ver sua tabuada: '))
cont = 0


print(f'=' * 15 + 'TABUADA' + '=' * 15)
while cont < 10:
    cont += 1
    resultado = n * cont
    print(f'{n} X {cont} = {resultado}')
print('=' * 37)
