from dataclasses import dataclass, asdict, astuple


@dataclass
class Pessoa:
    nome: str
    sobrenome: str


if __name__ == '__main__':
    p1 = Pessoa('LUIZ', 'OTAVIO')
    print(asdict(p1).items())
    print(astuple(p1)[0])
