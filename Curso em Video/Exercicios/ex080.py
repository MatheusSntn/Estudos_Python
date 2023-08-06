lista = []
cont = 0
for cont in range(0,5):
    n = int(input('Digite um número: '))
    if cont == 0 or n > lista[-1]: #pegar o ultimo valor
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'adicionado na posicao {pos} da lista...')
                break
            pos += 1
print('='*30)
print(f'Os valores digitados em ordem foram {lista}')