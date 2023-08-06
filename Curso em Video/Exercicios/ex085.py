cont = 0
par = list()
impar = list()
todos = list()
for cont in range(0,7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
impar.sort()
par.sort()
todos.append(par[:])
todos.append(impar[:])    
print(par)
print(impar)
print(todos)