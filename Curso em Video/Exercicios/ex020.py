import random
n1 = input('Insira um aluno: ')
n2 = input('Insira o segundo aluno: ')
n3 = input('Insira o terceiro aluno: ')
n4 = input('Insira o quarto aluno: ')
lista = [n1, n2, n3, n4]

print(lista)
random.shuffle(lista)
print('a ordem do trabalho será')
print(lista)
