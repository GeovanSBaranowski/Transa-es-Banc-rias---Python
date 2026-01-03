class conta:

    transacoes = []

    def __init__(self, saldo):
        self.saldo = saldo

    def saque(self):
        valor_saque = float(input('Qual o valor a ser sacado: '))

        if valor_saque < 0:
            print('Operacao negada')
            return self.saldo
        
        elif valor_saque <= self.saldo:
            print('Saque em execucao...')
            self.saldo -= valor_saque
            self.transacoes.append(f'saque: R${valor_saque}')
            return self.saldo
        
        else:
            print('Operacao negada! Valor de saque acima do saldo da conta')
            return self.saldo
        
    def deposito(self):
        valor_deposito = float(input('Qual o valor a ser depositado: '))

        if valor_deposito < 0:
            print('Operacao negada!')
        else:
            print('Deposito em execucao...')
            self.saldo += valor_deposito
            self.transacoes.append(f'deposito: R${valor_deposito}')
            return self.saldo
        
    def imprimir_extrato(self):
        
        print('-'*20)
        print("""
Extrato de Saques [1]
Extrato de Depositos [2]
Extrato de ambos os tipos [3]
                            """)
        print('-'*20)
        
        tipo_extrato = int(input('Escolha uma opcao: '))
        
        match tipo_extrato:
            case 1:
                for i in self.transacoes:
                    if 'saque' in i:
                        print(i)
            case 2:
                for i in self.transacoes:
                    if 'deposito' in i:
                        print(i)
            case 3:
                for i in self.transacoes:
                    print(i)

            case _ if tipo_extrato not in (1,2,3):
                print('Opcao invalida!')


conta1 = conta(2000)

def selecao_menu():

    while True:

        print('-'*20)
        print(""" 
Sacar [1]
Depositar [2]
Extrato [3]
Sair [0]
            """)  
        print('-'*20)  

        selecao = int(input('Escolha uma opcao: '))

        if selecao == 1:
            print('Iniciando operacao de saque...')
            conta1.saque()

        elif selecao == 2:
            print('Iniciando operacao de deposito...')
            conta1.deposito()

        elif selecao == 3:
            conta1.imprimir_extrato()

        elif selecao == 0:
            print('Operacao encerrada!')
            break
        else:
            print('Opcao invalida!')

selecao_menu()