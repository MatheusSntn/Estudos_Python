class A:
    def __new__(cls):
        print('Antes de criar a instancia')
        instancia = super().__new__(cls)
        print('depois')
        instancia.x = 234
        return instancia
    
    def __init__(self):
        print('Sou Init')

    def __repr__(self):
        return 'A()'
    
a = A()
print(a.x)