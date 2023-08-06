def titulo(txt):
    print('-'*30)
    print(txt)
    print('-'*30)


titulo('SISTEMA DE ALUNOS')
titulo('PYTHON É FODA')


def soma(a, b):
    s = a + b
    print(s)


soma(5, 9)
soma(8, 4)


def contador(*num):
    for valor in num:
        
        print(valor, end='')
    tam = len(num)
    print(' FIM' + f'\nO total de números inseridos foi {tam}')

contador(2, 1, 7)
contador(5, 7, 90)
contador(10, 20, 30, 40)

def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


valores = [1, 5, 2, 0, 10]
dobra(valores)
print(valores)

def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(7, 5)
soma(8, 9)