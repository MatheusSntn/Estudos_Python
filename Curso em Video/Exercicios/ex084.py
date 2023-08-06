mai_peso = men_peso = 0
galera = list()
pessoa = list()
while True:                    
    pessoa.append(str(input('Nome: ')))
    pessoa.append(int(input('Peso: ')))
    if len(galera) == 0:
        mai_peso = pessoa[1]
        men_peso = pessoa[1]        
    else:
        if mai_peso < pessoa[1]:
            mai_peso = pessoa[1]
        if men_peso > pessoa[1]:
            men_peso = pessoa[1]
    galera.append(pessoa[:])
    pessoa.clear()
    opcao = str(input('Deseja continuar: [S/N]')).strip().upper()
    if opcao == 'N':
        break
print(galera)
for p in galera:
    if mai_peso == p[1]:
            print(f'{p[0]}', end=' ')
    if men_peso == p[1]:
            print(f'{p[0]}', end=' ')
