lista = []
lista_par = []
lista_impar = []
cont = 0

while True:
    n = (int(input('Digite um número: ')))
    opcao = str(input('Deseja Continuar? [S/N] ')).strip().upper()[0]
    lista.append(n)
    cont += 1
    if opcao in 'SN':    
        if opcao == 'N':
            break
for n in lista:
    if n % 2 == 0:
        lista_par.append(n)
    else:
        lista_impar.append(n)

print(f'A lista completa é {lista}.')
print(f'A lista com valores pares é {lista_par}.')
print(f'A lista com valores impares é {lista_impar}.')

