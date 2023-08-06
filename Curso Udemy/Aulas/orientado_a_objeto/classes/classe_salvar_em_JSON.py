import json

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('Jonathan', 'Erick')

dados = [p1.__dict__]
def fazer_dump():
    print('fazendo dump')
    with open('salvandoclasse.json', 'w') as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    print('ELE EH O __main__')
    fazer_dump()