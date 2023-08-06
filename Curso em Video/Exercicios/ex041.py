from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano de nascimento: '))
cont = atual - nasc

if cont <= 9:
    print('MIRIM')
elif cont <= 14:
    print('INFANTIL')
elif cont <= 19:
    print('JUNIOR')
elif cont <= 25:
    print('SENIOR')
else:
    print('MASTER')
