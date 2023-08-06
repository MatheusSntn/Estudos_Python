# tabuada com numeros que o user digitar
while True:
    number = int(input('tell me a number for tabuada: '))
    if number < 0:
        break
    print('-' * 30)
    for c in range(1, 11):
        print(f'{number} X {c} = {number*c}')
    print('-' * 30)
print('obrigado volte sempre')
