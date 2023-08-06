class Multiplicar:
    def __init__(self, multiplicar):
        self._mult = multiplicar
    def __call__(self, func):
        def interna(*args, **kwargs):
            resultado = func(*args, **kwargs)
            return resultado
        return interna


@Multiplicar(10)
def soma(x, y):
   return x + y 

dois_mais_quatro = soma(2, 4)
print(dois_mais_quatro)