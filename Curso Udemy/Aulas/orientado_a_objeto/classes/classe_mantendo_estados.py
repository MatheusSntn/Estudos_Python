class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando
    
    def Filmar(self):
        if self.filmando:
            print(f'{self.nome} JÁ está filmando...')
            return
        print(f'{self.nome} está filmando...') 
        self.filmando = True
    
    def PararFilmar(self):
        if not self.filmando:
            print(f'{self.nome} NÃO está filmando...')
            return
        print(f'{self.nome} está parando de filmar')
        self.filmando = False

    def Fotografar(self):
        if self.filmando:
            print(f'{self.nome} não pode fotografar filmando')
            return
        print(f'{self.nome} está fotografando')
        

c1 = Camera('Canon')
c2 = Camera('Sony')
c1.Filmar()
c1.Filmar()
c1.PararFilmar()
c1.Fotografar()
print()
c2.PararFilmar()
c2.Filmar()
c2.Filmar()
