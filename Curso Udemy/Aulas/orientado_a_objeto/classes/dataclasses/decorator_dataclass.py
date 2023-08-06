from dataclasse import dataclass

# init=false - desabilita o init
# frozen=true - vai congelar sua classe, impossivel de setar coisas


# @dataclass(repr=True, order=True)
# class Pessoa:
#     nome: str
#     sobrenome: str


# if __name__ == '__main__':
#     p1 = [Pessoa('A', 'Z'), Pessoa('B', 'Y'), Pessoa('C', 'X')]
#     ordenadas = sorted(p1, reverse=True)
#     print(ordenadas)

@dataclass(repr=True)
class Pessoa:
    nome: str
    sobrenome: str


if __name__ == '__main__':
    p1 = [Pessoa('A', 'Z'), Pessoa('B', 'Y'), Pessoa('C', 'X')]
    ordenadas = sorted(p1, reverse=True, key=lambda p: p.sobrenome)
    print(ordenadas)
