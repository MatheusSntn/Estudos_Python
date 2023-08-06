class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self,nome):
        print(nome, 'esta Chamando, ', self.phone)
        return 1234

call1 = CallMe('23343554657')
retorno = call1('Luiz otavio')
print(retorno)