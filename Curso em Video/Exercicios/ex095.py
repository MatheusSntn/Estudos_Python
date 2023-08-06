galera = list()
jogador = dict()
gols = list()

jogador['nome'] = str(input('NOME DO JOGADOR: '))
tot = int(input(f'NUM DE PARTIDAS JOGADAS POR {jogador["nome"]}: '))
for c in range(0, tot):
    gols.append(int(input(f'Quantos gols na partida {c}: ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(jogador['gols'])

print(jogador)

print('=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('=' * 30)

print(f'o jogador {jogador["nome"]} jogou {tot} Partidas')

for i, v in enumerate(jogador['gols']):
    formatado = print(f'\t ==> Na partida {i}, fez {v} Gols.' )
print(f'Foi um total de {jogador["total"]} gols.')