class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    def lista_endereco(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)
    

class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero
    
    def __del__(self):
        print('Apagando', self.rua, self.numero) #garbit colection (coleta e recolhe o lixo da memoria)

cliente1 = Cliente('Maria')
cliente1.inserir_endereco('av Brasil', 54)
cliente1.inserir_endereco('b', 543)
cliente1.lista_endereco()

print('AQUI TERMINA MEU CODE')
