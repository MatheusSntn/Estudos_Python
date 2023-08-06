tot50 = tot20 = tot10 = tot1 = 0

print('=' * 30)
print('{:^30}'.format('CAIXA'))
print('=' * 30)

while True:
    saque = float(input('Quanto voce quer sacar? R$'))
    print('=' * 30)
    resto = saque
    if saque >= 50:
        divisao = saque // 50
        resto = saque % 50
        tot50 += divisao
        if tot50 > 0:
            print(f'Total de cedulas de R$50: {tot50}')
        #print(resto)
    if saque or resto >= 20:
        divisao = resto // 20
        resto = resto % 20
        tot20 += divisao
        if tot20 > 0:
            print(f'Total de cedulas de R$20: {tot20}')
        #print(resto)
    if saque or resto >= 10:
        divisao = resto // 10
        resto = resto % 10
        tot10 += divisao
        if tot10 > 0:
            print(f'Total de cedulas de R$10: {tot10}')
        #print(resto)
    if saque or resto >= 1:
        divisao = resto // 1
        resto = resto % 1
        tot1 += divisao
        if tot1 > 0:
            print(f'Total de cedulas de R$1: {tot1}')
        #print(resto)
        print('=' * 30)
    if resto == 0:
        break




