import contas


class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'{self.nome!r}, {self.idade!r}'
        return f'{class_name} ({attrs})'


class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        self.conta: contas.Conta | None = None  # | = OU


if __name__ == '__main__':
    c1 = Cliente('Luiz', 30)
    print(c1)
    c1.conta = contas.ContaCorrente(111, 222, 0, 0)
    print(c1.conta)

    c2 = Cliente('Maria', 18)
    c2.conta = contas.ContaPoupanca(112, 223, 0)
    print(c2)
    print(c2.conta)
