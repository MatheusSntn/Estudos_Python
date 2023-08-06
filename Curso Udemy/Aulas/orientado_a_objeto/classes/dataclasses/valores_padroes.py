from dataclasses import dataclass, field, fields


@dataclass
class Pessoa:
    name: str = field(
        default='Missing'
    )
    sobrenome: str = 'not find'
    idade: int = 0
    enderecos: list[str] = field(default_factory=list)


if __name__ == '__main__':
    p1 = Pessoa()
    print(fields(p1))
    # print(p1)
