import random
import time

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
number = random.choice(numbers)

adivinhe = int(input('Em que número eu pensei? '))

if number == adivinhe:
    print('VOCE ACERTOU, PARABENS')
else:
    print(f'Tente novamente. Eu pensei no número {number}')

# OU

computador = random.randint(1, 10)  # Faz o Computador sortear de 1 a 10
print('-=-' * 20)
print('Pensarei em um número entre 0 e 10, tente adivinhar...')
print('-=-' * 20)

jogador = int(input('Em qual número eu pensei? '))
print('PROCESSANDO...')
time.sleep(3)
if jogador == computador:
    print('PARABENS! Voce acertou!')
else:
    print('Voce errou! Eu pensei no número {} não no número {}'.format(
        computador, jogador))
