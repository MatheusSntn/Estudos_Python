from random import randint
from operator import itemgetter

jogo = dict()
ranking = list()

jogo['jogador1'] = randint(0, 10)
jogo['jogador2'] = randint(0, 10)
jogo['jogador3'] = randint(0, 10)
jogo['jogador4'] = randint(0, 10)
print('valores sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou {v}.')

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(ranking)

for i, v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} com {v[1]}')



