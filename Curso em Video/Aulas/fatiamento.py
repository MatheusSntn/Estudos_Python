frase = 'curso em video python'
# frase[9:21] #Com range o ultimo valor n entra na contagem

print(len(frase))
print(frase.count('o', 0, 13))
print(frase.find('deo'))
print(frase.find('android'))
'curso' in frase
print(frase.replace('python', 'android'))
print(frase.strip())  # remove os espacoes a direita e esquerda (espacos inuteis)
print(frase.split())  # divide a frase em seus espacos, criando uma lista
''.join(frase)
print(frase)
