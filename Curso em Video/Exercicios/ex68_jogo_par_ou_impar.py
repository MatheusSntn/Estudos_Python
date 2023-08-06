from random import randint

v = 0

while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '

# enquanto tipo não é PpIp
    while tipo not in 'PI':
        # coleta somente a primeira letra
        tipo = str(input('par ou ímpar? [P/I]')).strip().upper()[0]
    print(
        f'voce jogou {jogador} e o computador {computador}, totalizando {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('voce venceu')
            v += 1
        else:
            print('voce perdeu')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('voce venceu')
            v += 1
        else:
            print('voce perdeu')
            break
    print('vamos jogar novamente')
print('-' * 30)
print(f'Game Over! voce venceu {v} vezes')
print('-' * 30)
