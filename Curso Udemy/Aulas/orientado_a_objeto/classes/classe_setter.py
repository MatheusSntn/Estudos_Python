class Caneta:
    def __init__(self, cor): 
        self._cor = cor

    @property
    def cor(self):
        print('PROPERTY') 
        return self._cor
    
    @cor.setter
    def cor(self, valor):
        print('ESTOU NO SETTER', valor)
        self._cor = valor

c1 = Caneta('azul')
c1.cor = 'rosa'
print(c1.cor)