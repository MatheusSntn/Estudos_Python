salario = float(input('digite seu salario: R$'))
reajuste = salario + (salario*15/100)

print(
    f'seu salario era R${salario:.2f} e com o reajuste ficou: {reajuste:.2f}')
