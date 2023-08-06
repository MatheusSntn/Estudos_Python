n = int(input('Digite quantos termos voce quer mostrar: '))
t1 = 0
t2 = 1
print(f'{t1} -> {t2}', end=' -> ')
cont = 3
while cont <= n:
    t3 = t1 + t2
# passagem dos termos, mudanca de valor dos termos apos a soma:
    t1 = t2
    t2 = t3
    cont += 1
    print(t3, end='-> ')
