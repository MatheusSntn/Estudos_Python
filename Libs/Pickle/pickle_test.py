import pickle

# x = [1, 2, 3, 4]

class Pessoa:
    nome = 'caio'
    idade = 12

class Pessoas:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoas('Joao Gomes', '41')

# arq = open('arquivo.pickle', 'wb')
# pickle.dump(obj=x, file=arq)

# arq = open('arquivo.pickle', 'rb')
# returno = pickle.load(arq)

# print(returno)

with open('arquivo4.pickle', 'wb') as arq:
    pickle.dump(p1, arq)

with open('arquivo4.pickle', 'rb') as arq:
    arq = pickle.load(arq)
    print(arq.idade)