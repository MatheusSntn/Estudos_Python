termo = int(input('Digite o termo: '))
razao = int(input('Digite a razao: '))
decimo = termo + (10 - 1) * razao
for cont in range(termo, decimo + razao, razao):
    print(cont, end=' > ')
print('FIM')
