n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))
n3 = int(input('Digite um valor: '))
n4 = int(input('Digite um valor: '))
numbers = (n1,n2,n3,n4)
cont = 0

print(numbers)
for n in numbers:
    if n == 9:
        cont += 1
    if n == 3:
        pos3 = numbers.index(3, 0)
print(f'Quantas vezes apareceu o valor 9: {cont} vezes. ')
print(f'Em que posição foi digitado o primeiro valor 3: {pos3}')
print(f'Foram os numeros pares:',)
for par in numbers:
    if par % 2 == 0 and n != 0:
        print(par, end=' ' )

