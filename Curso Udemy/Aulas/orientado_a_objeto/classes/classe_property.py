class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    @property
    def cor(self):
        print('Property')
        return 'Qualquer cor'

    @property
    def cor_tampa(self):
        return 123456
#def get_cor(self):
#print('GET COR')
#return self.cor_tinta
    

caneta = Caneta('Azul')
print(caneta.cor)
print(caneta.cor_tampa)