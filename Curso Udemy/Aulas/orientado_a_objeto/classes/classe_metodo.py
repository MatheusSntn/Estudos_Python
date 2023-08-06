# Métodos em instancias de classes Python
# Hard Coded = É algo que foi escrito diretamente no codigo
class Carro:
    def __init__(self, nome='sei la'):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...')

fusca = Carro('fusca')
print(fusca.nome)
fusca.acelerar()

celta = Carro(nome='celta')
print(celta.nome)
celta.acelerar()

