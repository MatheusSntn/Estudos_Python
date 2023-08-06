
stop = 999
tot_n = 0
cont = 0
active = True

while active:
    n = int(input('Digite um número: '))
    if n == stop:
        active = False
    else:
        tot_n += n
        cont += 1
print(tot_n, cont)
