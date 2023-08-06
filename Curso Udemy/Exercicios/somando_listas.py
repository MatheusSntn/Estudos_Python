l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = [1, 2, 3, 4, 5]

def soma_l(l1, l2):
    intervalo = min(len(l1), len(l2)) # faz o minimo entre l1 e l2
    # atraves de listcomprehension, soma cada um dos valores
    # até o intervalo:
    return [(l1[i] + l2[i])
    for i in range(intervalo)
    ] 

lista_soma = soma_l(l1, l2)

print(lista_soma)

# OU SEM FUNCAO

lista_soma  = [2, 4, 6, 8]

lista_a = [10, 2, 3, 40, 5, 6, 7]
lista_b = [1, 2, 3, 4]
lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
print(lista_soma)