cont = 0
tot_n = maior_n = menor_n = 0
stop = 'N'
active = True

while active:
    n = int(input('Digite um número: '))
    cont += 1
    tot_n += n
    if cont == 1:
        maior_n = menor_n = n
    else:
        if n > maior_n:
            maior_n = n
        if n < menor_n:
            menor_n = n
    opcao = str(input('Deseja continuar [S/N]')).strip().upper()[0]
    if opcao == stop:
        active = False

media = tot_n / cont
print(f'Voce digitou {cont} números')
print(f'A média foi {media}.')
print(f'O maior valor foi {maior_n} e o menor {menor_n}.')
