class Pessoa:
    ano = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('Hey')

    @classmethod
    def criar_sem_nome(cls, nome):
        return cls(nome)
    
    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)

p1 = Pessoa('Joao', 34)
p2 = Pessoa.criar_com_50_anos('Helena')
p3 = Pessoa('Anonima', 23)
p4 = Pessoa.criar_sem_nome
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
print(Pessoa.metodo_de_classe())
