#iterator infinito
#atravez de um metodo

from itertools import count

c1 = count(10)
r1 = range(10, 100)

print(next(c1))
print(next(c1))

print('c1', hasattr(c1, '__iter__'))


for i in c1:
    if i > 100:
        break
    print(i)

print()
print()
print()

for i in r1:
    print(i)