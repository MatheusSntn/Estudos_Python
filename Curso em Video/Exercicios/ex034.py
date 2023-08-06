salario = float(input('digite seu salario: R$'))
if salario >= 1250:
    aumento = salario + (salario*10/100)
    print(
        f'Com o aumento de 10 por cento seu salario será de: R${aumento:.2f}')
else:
    aumento = salario + (salario*15/100)
    print(
        f'Com o aumento de 15 por cento seu salario será de: R${aumento:.2f}')
