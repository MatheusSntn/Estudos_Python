n_extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito')
for n in n_extenso:
    num = int(input('digite um numero entre 0 e 8: '))
    if num <= 8:
        print(f'o número digitado foi {n_extenso[num]}')
    if num > 8:
        num = int(input('por favor, digite um numero entre 0 e 8: '))
        print(f'o número digitado foi {n_extenso[num]}')
        