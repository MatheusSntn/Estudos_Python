import random
cont = 0
while True:
    par_pc = impar_pc = par_pl = impar_pl = 0 
    computador = random.randint(1, 11)
    n = int(input('Digite um número: '))
    opcao = str(input('Escolha Par ou Impar [P/I]: ')).strip().upper()[0]
    if opcao == 'P':
        if (n + computador) % 2 == 0:
            print(f'{n} + {computador} = {n + computador}')
            print('O número é par. VOCE GANHOU!')
            cont += 1
        if (n + computador) % 2 == 1:
            print(f'{n} + {computador} = {n + computador}')
            print('O número é impar. VOCE PERDEU!')
            break    
    if opcao == 'I':
        if (n + computador) % 2 == 1:
            print(f'{n} + {computador} = {n + computador}')
            print(f'O número é impar. VOCE GANHOU!')
            cont += 1
        if (n + computador) % 2 == 0:
            print(f'{n} + {computador} = {n + computador}')
            print(f'O número é par. VOCE PERDEU!')
            break
print(f'Game Over. Voce venceu {cont} vezes.')