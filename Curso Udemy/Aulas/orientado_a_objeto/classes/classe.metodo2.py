# Escopo da classe e de metodos da classe
class Animal:
    #nome = 'leao'
    def __init__(self, nome):
        self.nome = nome
    
    def comendo(self, alimento):
        return f'{self.nome} está comendo {alimento}'
    
    def executar(self, *args):
        return self.comendo(*args)
        

leao = Animal(nome='Bufalo')
print(leao.nome)
print(leao.executar('ave'))