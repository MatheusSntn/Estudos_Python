'''frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()  # cria lista das palavras (separa no espaco)
junto = ''.join(palavras)  # junta as palavras dessa lista
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f'o inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')'''


# OU (Macete do python)

frase = str(input('Digite uma frase: '))
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print(f'O inverso de {junto} é {inverso}.')
if inverso == junto:
    print('Temos um palindromo!')
else:
    print('Não temos um palindromo!')
