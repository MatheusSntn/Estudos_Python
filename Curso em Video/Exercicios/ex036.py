casa = float(input('valor da casa: '))
salario = float(input('qual o seu salario: '))
anos = float(input('em quantos anos será pago: '))
cont_prestacao = casa / (anos*12)
cont_salario = salario * 30/100

print(cont_prestacao)
print(cont_salario)

if cont_prestacao <= cont_salario:
    print('Emprestimo sera concedido')
else:
    print('Nao podemos aceitar esse emprestimo')
