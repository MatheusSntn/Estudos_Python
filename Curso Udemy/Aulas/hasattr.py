# verifica se metodo existe na funcao

string = 'luiz'
 
if hasattr(string, 'upper'): # metodo vem em aspas
    print('Existe Upper')
    print(string.upper())

# ou faca isso dinamincamente (mas tem que ta em aspas):
string = 'Luiz'
metodo = 'upper'
if hasattr(string, metodo):
    print('Existe upper')
    print(getattr(string, metodo)()) # Faz o python dizer se tem ou n o metodo
else:
    print('Não existe o metodo')

