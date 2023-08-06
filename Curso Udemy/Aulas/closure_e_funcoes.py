def saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

s1 = saudacao('bom dia')
s2 = saudacao('boa noite')
print(s1('joao'), s2('jonathans'))

for nome in ['joao', 'pedro', 'gui']:
    print(s1(nome))
    