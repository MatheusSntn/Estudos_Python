loja = ('Borracha', 2.90,
        'lapis', 15.90,
        'caderno', 10.00,
        'estojo', 5.00)
for item in range(0, len(loja)):
    if item % 2 == 0:
        print(f'{loja[item]:.<30}:.', end='') 
    else:
        print(f'R${loja[item]:>7.2f}')