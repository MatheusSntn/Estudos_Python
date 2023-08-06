print('-=-' * 10)
print(' ' * 10 + 'CONVERSOR')
print('-=-' * 10)


n = int(input('Digite um número: '))
print('Escolha uma base de conversao: ')
choice = int(input('''[ 1 ] Converter para Binario
[ 2 ] Converter para Octal
[ 3 ] Converter para Hexadecimal'''))
if choice == 1:
    print('o numero {} em binário é {}'.format(n, bin(n)[2:]))
elif choice == 2:
    print('o numero {} em binário é {}'.format(n, oct(n)[2:]))
elif choice == 3:
    print('o numero {} em binário é {}'.format(n, hex(n)[2:]))
else:
    print('opcao invalida')
