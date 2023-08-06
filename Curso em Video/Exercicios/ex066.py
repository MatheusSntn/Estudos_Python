s = cont = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
    cont +=1
print(f'A soma dos valores deu {s}')
print(f'O total de valor digitado foi {cont}')
print('Acabou.')
