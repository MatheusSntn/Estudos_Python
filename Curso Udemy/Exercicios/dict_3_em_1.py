import copy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


print(*produtos, sep='\n')

print()

novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)}
    for p in copy.deepcopy(produtos)
]
print()

print(*novos_produtos, sep='\n')
#print(*novos_produtos, sep='\n')

produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos), 
    key=lambda p: p['nome'],
    reverse= True
)

print()
print()

print(*produtos_ordenados_por_nome, sep='\n')
