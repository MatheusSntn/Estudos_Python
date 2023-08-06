import json

from classe_salvar_em_JSON import Pessoa, fazer_dump

fazer_dump()

with open("salvandoclasse.json") as arquivo:
    pessoas = json.load(arquivo)
    p1 = Pessoa(**pessoas[0])

    print(p1.nome, p1.sobrenome)
