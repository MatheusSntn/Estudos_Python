cont = 0
num = int(input('Digite um número: '))
tot = 0

for cont in range(1, num + 1):
    if num % cont == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print(cont, end=' ')
print(f'\nO número {num} foi divisivel {tot} vezes')
if tot == 2:
    print(f'{num} número primo')
else:
    print(f'{num} não é primo.')

# OR
total = 0
for cont in range(1, num + 1):
    print(cont, end=' ')
    if num % cont == 0:
        total += 1
if total == 2:
    print('numero primo')
else:
    print('\nnúmero nao primo')
