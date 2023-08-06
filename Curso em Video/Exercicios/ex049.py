mult = 0
cont = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    mult += 1
    result = cont * mult
    print(f'{cont} X {mult} = {result}')

# OU

num = int(input('Digite um numero para ver sua tabuada: '))
for c in range(1, 11):
    print(f'{num} X {c} = {num*c}')

