def generation(n=0):
    yield 1 # Pausar
    print('Continuando')
    yield 2 # Pausar
    print('Continuando')
    yield 3 # Pausar
    print('Vou terminar')
    return 'Acabou'

gen = generation(n=0)
#print(next(gen))
#print(next(gen))
#print(next(gen))
#print(next(gen))

# AUTOMATICAMENTE
for n in gen:
    print(n)

def generation(n=0, maximum=10):
    while True:
        yield n
        n += 1
        if n >= maximum:
            return

gen = generation(n=0)
for n in gen:
    print(n)