produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

for produto in produtos:
    print(produto)

print()

novos_produtos = [
    produto
    for produto in produtos
]

print(*novos_produtos, sep='\n')

print()

# alterando valores:
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    for produto in produtos
]

print(*novos_produtos, sep='\n')

print()

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else produto['preco']
    for produto in produtos
]

print(*novos_produtos, sep='\n')

novos_produtos = [
    {**produto, 'preco':produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if (produto['preco'] >= 20 and produto['preco'] * 1.05) > 10
]
print(*novos_produtos, sep='\n')

lista = [
    (x, y) # MAPEAMENTO
    for x in range(3)
    for y in range(3)
]
print(*lista, sep='\n')