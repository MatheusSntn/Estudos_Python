# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos

from itertools import combinations, permutations, product

pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
]

camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'poliéster']
]

def print_iter(iterator):
    print(*list(iterator), sep = '\n')
    print()

# forma todos os grupos de 2 ( ou outro valor) 
# possiveis com as pessoas da lista 
print_iter(combinations(pessoas, 2))

# combinacoes em grupos que podem se repetir
print_iter(permutations(pessoas, 2))

# combinacaoes de produtos
print_iter(product(*camisetas))

