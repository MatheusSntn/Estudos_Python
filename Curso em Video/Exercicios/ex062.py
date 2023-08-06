n = int(input('Digite um número: '))
r = int(input('Digite a razão: '))
cont_1 = 1
soma = 0
print(n, end='-> ')
while cont_1 < 10:
    n += r
    cont_1 += 1
    print(n, end='-> ')

opcao = 1
totopcao = 10
while opcao != 0:
    cont_2 = 1
    opcao = int(
        input('''\nPreciose '0' para sair ou algum número para continuar: '''))
    totopcao = totopcao + opcao
    while cont_2 <= opcao:
        n += r
        cont_2 += 1
        print(n, end='-> ')
print('FIM')
print(f'Progressao finalizada com {totopcao} mostradas.')
