n = int(input('Digite um número: '))
r = int(input('Digite a razão: '))
cont = 1
soma = 0
print(n, end='-> ')
while cont < 10:
    n += r
    cont += 1
    print(n, end='-> ')
print('FIM')
