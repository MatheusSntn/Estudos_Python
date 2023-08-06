matriz = ([0, 0, 0], [0, 0, 0], [0, 0, 0])
spar = ster = maior2 = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz [l][c] = int(input(f'digite um valor para {l} {c}: '))

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c] 
    print()

for l in range(0,3):
    ster += matriz[l][2]
    for c in range(0, 3):
        maior2 = matriz[1][0]
        if maior2 < matriz[1][c]:
            maior2 = matriz[1][c]

print(spar)
print(ster)
print(maior2)

