num = []
maior= menor = 0


for cont in range(0, 5):
    num.append(int(input('Digite um valor: ')))
    if cont == 0:
        maior = menor = num[cont]
    else:
        if num[cont] > maior:
            maior = num[cont]
        if num[cont] < menor:
            menor = num[cont]
print(f'o maior valor foi {maior} e está na posicao ', end='')
for cont, v in enumerate(num):
    if v == maior:
        print(f'{cont}... ', end='')
print()
print(f'o menor valor foi {menor} e está na posicao ', end='')
for cont, v in enumerate(num):
    if v == menor:
        print(f'{cont}... ', end='')



'''    num.append(int(input('Digite um valor: ')))
    maior = num[0]
    menor = num[0]
    for n in num:
        if maior < n:
            maior = n
        if menor > n:
            menor = n
print(maior)
print(menor)'''    
#print(max(num))
#print(min(num))
     
 