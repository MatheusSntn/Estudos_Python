# namedtuples - tuplas imutáveis com nomes para valores
# Usamos namedtuples para criar classes de objetos que são apenas um
# agrupamento de atributos, como classes normais sem métodos, ou registros de
# bases de dados, etc.
# As namedtuples são imutáveis assim como as tuplas.
# https://docs.python.org/3/library/collections.html#collections.namedtuple
# https://docs.python.org/3/library/typing.html#typing.NamedTuple
# https://brasilescola.uol.com.br/curiosidades/baralho.htm
# from collections import namedtuple

from typing import NamedTuple


class Carta(NamedTuple):
    valor: str = 'VALOR'
    naipe: str = 'NAIPE'


# Carta = namedtuple('Carta', ['Valor', 'Naipe'],
#                    defaults=['VALOR', 'NAIPE']
#                    )
as_espadas = Carta('A', 'Espadas')

print(as_espadas._asdict())
# print(as_espadas)
# print(as_espadas.Naipe)
# print(as_espadas.Valor)
print(as_espadas._fields)
print(as_espadas._field_defaults)
