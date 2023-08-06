import random

number = range(1, 11)
computador = random.choice(number)
player = int(input('Digite um número: '))
cont = 0

while player != computador:
    if player > computador:
        print('Errado. É um número menor!')
        player = int(input('Digite outro número: '))
        cont += 1
    if player < computador:
        print('Errado. É um número maior!')
        player = int(input('Digite outro número: '))
        cont += 1
print(f'Voce acertou na {cont} tentativa. Parabens!!')
