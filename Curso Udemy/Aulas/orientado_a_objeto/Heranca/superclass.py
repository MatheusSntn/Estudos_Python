# Criar classe "sombra"

class MinhaString(str):
    def upper(self): #essa funcao faz com que o upper que ja existe 
                     #na classe str nunca seja executado
                     #e eh executado apenas esse
        print('Chamou Upper')
        return super().upper() #COM O "SUPER" EU CONSIGO
                               #POIS CHAMO A SUPERCLASSE
    


string =  MinhaString('Jef')
print(string.upper())

class A:
    atributo_a = 'valor a'

    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        print(A)

class B(A):
    atributo_b = 'valor b'

    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo) # repassando init pro A
        self.outra_coisa = outra_coisa # colocando algo a mais no B

    def metodo(self):
        print(B)

class C(B):
    atributo_c = 'valor c'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('Burlei o sistema.')

    def metodo(self):
        print(C)

c = C('aaaaaaaaaaaa', 'qualquer')
print(c.atributo)
print(c.outra_coisa)

# print(c.atributo_c)
# print(c.atributo_b)
# print(c.atributo_a)

# print(C.mro())
# Geralmente, serve para extender uma funcionalidade
