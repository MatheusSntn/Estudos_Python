lista = []
cont = 0


while True:
    lista.append(int(input('Digite um número: ')))
    opcao = str(input('Deseja Continuar? [S/N] ')).strip().upper()[0]
    cont += 1
    if opcao in 'SN':    
        if opcao == 'N':
            break

if 5 in lista:
    print('O valor 5 foi digitado na lista.')
else:
    print('O valor 5 não foi digitado na lista.')   

print(f'foram digitados {cont} números.')
print(sorted(lista, reverse=True))

