set1 = {1, 2, 3}
set2 = {2, 3, 4}
set3 = set1 | set2 # unir sets
set3 = set1 & set2 # mostra os itens presentes em ambos
set3 = set1 - set2 # mostra itens disponiveis apenas no set da esquerda
set3 = set1 ^ set2 # itens que nao estao presentes em ambos

print(set3)

letras = set()
while True:
    letra = input('digite: ')
    letras.add(letra.lower())

    if 'l' in letras:
        print('Parabens')
        break

    print(letras)