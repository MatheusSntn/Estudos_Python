tabuada = 'tabuada'
print('=' * 20)
print(f'{tabuada:^20}')
print('=' * 20)
while True:
    cont = 0 
    n = int(input('Digite um número: '))
    if n <= 0:
        break
    while cont <= 10:
        print(f'{n} X {cont} = {n * cont}')
        cont += 1
