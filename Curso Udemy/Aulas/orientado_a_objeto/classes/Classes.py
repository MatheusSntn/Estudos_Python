# metodos em instancia de classes Python
class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('luiz', 'Otávio')
p2 = Pessoa('Maria', 'Joana')

print(f'{p1.nome}\n{p1.sobrenome}')
print(f'{p2.nome}\n{p2.sobrenome}')