from time import sleep

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

active = True
while active:
    print('=' * 30)
    print(' ' * 5 + 'ESCOLHA UMA OPERACAO')
    print('=' * 30)
    print('-=-' * 10)
    print('''[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA''')
    print('-=-' * 10)
    opcao = int(input('Escolha uma operacao: '))

    if opcao == 1:
        somar = n1 + n2
        print(f'{n1} + {n2} = {somar}')
        sleep(1)
    elif opcao == 2:
        multiplicar = n1 * n2
        print(f'{n1} * {n2} = {multiplicar}')
        sleep(1)
    elif opcao == 3:
        maior = n1
        if n2 > n1:
            maior = n2
        print(f'O maior número é {maior}')
        sleep(1)
    elif opcao == 4:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
    elif opcao == 5:
        active = False
