def mult (*args):
    total = 1
    for numeros in args:
        total *= numeros
    return total
    

total1 = mult(1, 2, 3, 4, 5)
print(total1)

def par_impar(a):
    if a % 2 == 0:
        return f'{a} é par'
    return f'{a} é impar'

print(par_impar(2))
print(par_impar(3))