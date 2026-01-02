
def selecao_menu():

    print(""" 
Sacar [1]
Depositar [2]
Extrato [3]
Sair [0]
""")

    while True:

        selecao = int(input('Escolha uma opcao: '))

        if selecao == 1:
            print('Iniciando operacao de saque')
            return False
        elif selecao == 2:
            print('Iniciando operacao de deposito')
            return False
        elif selecao == 3:
            print('Imprimindo extrato')
            return False
        elif selecao == 0:
            print('Operacao encerrada')
            break
        else:
            print('Opcao invalida')


selecao_menu()