import time
import random

print('-=-' * 15)
print(' ' * 15 + 'JOKENPO!!')
print('-=-' * 15)
print('''[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TISOURA''')

e012 = ['PEDRA!', 'PAPEL!', 'TISOURA!']

escolha = int(input(('\nEscolha um Número: ')))
escolha_pc = random.randint(0, 2)
print(e012[escolha])
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!')
print(e012[escolha_pc])

if escolha == escolha_pc:
    print('EMPATE! Jogue novamente.')
elif escolha == 0 and escolha_pc == 1:
    print('VOCE PERDEU! COMPUTADOR WIN!!!')
elif escolha == 0 and escolha_pc == 2:
    print('VOCE GANHOU!')
elif escolha == 1 and escolha_pc == 0:
    print('VOCE GANHOU!')
elif escolha == 1 and escolha_pc == 2:
    print('VOCE PERDEU! COMPUTADOR WIN!!!')
elif escolha == 2 and escolha_pc == 0:
    print('VOCE PERDEU! COMPUTADOR WIN!!!')
elif escolha == 2 and escolha_pc == 1:
    print('VOCE GANHOU!')
