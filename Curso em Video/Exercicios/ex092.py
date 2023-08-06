from datetime import datetime

registro = dict()

registro['nome'] = str(input('Digite o nome: '))
registro['ano'] = int(input('Digite seu ano de nascimento: '))
nasc = registro['ano']
registro['idade'] = datetime.now().year - nasc
registro['ctps'] = int(input('Digite sua CTPS: '))

if registro['ctps'] != 0:
    registro['ano_contrat'] = int(input('digite seu ano de contrato: '))
    registro['salario'] = int(input('Digite seu salario: '))
    registro['aposentadoria'] = (registro['ano_contrat'] + 35) - datetime.now().year

for k, v in registro.items():
    print(f'{k} = {v}')
