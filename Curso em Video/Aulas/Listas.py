'''num = list(range(4,8))
num[2] = 6
num.append(8)
num.insert(2,0)
num.pop(0)
print(num)
print(f'essa lista tem {len(num)} elementos')

if 7 in num:
    num.remove(7)
    print(num)
else:
    print('Nao achei o 4')

valores = []
valores.append(1)
valores.append(3)
valores.append(6)
print(valores)

for c, v in enumerate(valores):
    print(f'na posicao {c} encontrei o valor {v}...', end='\n')
print('cheguei no final da lista')

valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posicao {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')'''

a = [2, 3, 4, 7]
b = a #ligacao de listas
b[2] = 8 

print(f'Lista A: {a}')
print(f'Lista B: {b}')

c = [2, 3, 4, 7]
d = [2, 3, 4, 7]
c = d[:] #copia de lista
d[2] = 8
print(f'Lista C: {c}')
print(f'Lista D: {d}')