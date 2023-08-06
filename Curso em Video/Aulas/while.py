n = 1
par = 0
impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n % 2:
        par += 1
    else:
        impar += 1
print(f'vc digitou {par} números pares.')
print(f'voce digitou {impar} números impares.')
