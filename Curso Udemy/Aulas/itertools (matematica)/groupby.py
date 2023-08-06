from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

# groupby (grupo por) - é necessário ordenar antes, por isso
# segue funcao:
def ordena(aluno):
    return aluno['nota'] # ordenado por nota

alunos_agrupados = sorted(alunos, key=ordena)
grupos = groupby(alunos_agrupados, key=ordena)

for chave, valor in grupos:
    print(chave)
    for aluno in valor:
        print(aluno)

exemplo_mais_simples = ['a', 'a', 'b', 'b', 'c']
grupos = groupby(exemplo_mais_simples)

print()
print()
print()


for chave, valor in grupos:
    print(chave)
    print(list(valor))