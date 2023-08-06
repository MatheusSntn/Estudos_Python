def gen1():
    yield 1
    yield 2
    yield 3
    print('acabou o gen1')

def gen2():
    print('Comecou o gen2')
    yield from gen1()
    yield 4
    yield 5
    yield 6

g = gen2()
for n in g:
    print(n)
