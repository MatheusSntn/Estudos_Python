print('Comandos: listar, desfazer, refazer')

cont = 0
lista = []
teste = []

while True:    
    opcao = input('Digite uma tarefa ou comando: ')
    print('TAREFAS: ')
    lista.append(opcao)
    if opcao == 'desfazer':
        jao = lista.pop(-1)
        jao = lista.pop(-1)
    if opcao == 'refazer':
        lista.pop()
        lista.append(jao)
    for i in lista:
        print(i)
  
