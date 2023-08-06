dados = dict()


for d in range(0, 1):
    dados['nome'] = str(input('Digite o nome do aluno: '))
    dados['media'] = float(input(f'Digite a média do {dados["nome"]}: '))
    if dados['media'] > 7:
        dados['situacao'] = 'Aprovado'
    else:
        dados['situacao'] = 'Reprovado'
    print(dados)

for k, v in dados.items():
    print(f'{k} = {v}')
