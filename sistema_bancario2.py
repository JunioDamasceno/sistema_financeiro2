#Programa desenvolvido para atividade do curso "Potência Poweded by Ifood | Ciência de dados" da DIO

#Programa simples que simula três operações básicas de um sistema bancário: Depósito, saque e extrato
#Regra 1: Não pode haver saques e depósitos em valor negativo
#Regra 2: Não é possível sacar valor maior que R$ 500,00 por operação
#Regra 3: Não é permitida mais que três operações de saque

#para dar clear no terminal quando o sistema for fechado.
from os import system
#Para registrar data e hora no sistema quando for gravadas as operações de saque ou depósito.
from datetime import datetime

saldo = 0
limval_saque = 500
extrato = []
i = 0
j = 0
nsaques = 0
lim_saques = 3
opcao = ''
usuarios = []
contas = []
agencia = "0001"
nconta = 0

def menu():
    menu = """
    Escolha uma das opções abaixo:
    
    [nu] Novo usuário
    [nc] Nova Conta
    [ls] Listar Contas
    [d]  Depositar
    [s]  Sacar
    [e]  Extrato
    [q]  Sair
    Ditige a opção: """
    return(input(menu))

def novo_usuario():
    cpf = input("Informe o seu CPF: ")
    consulta = filtrar_usuarios(cpf, usuarios)
    if consulta == None:
        nome = input("Informe o nome completo: ")
        dt_nascimento = input("Informe a data de nascimento (DD/MM/AAAA): ")
        endereco = input("Informe o endereço completo (Logradouro, nº, bairro, Cidade, Estado): ")
        usuarios.append({"Nome": nome, "CPF": cpf, "Data de Nascimento": dt_nascimento, "Endereço": endereco})
        return (print("\n*** Usuaŕio cadastrado com sucesso! ***"))
    else: 
        return(print("CPF já cadastrado para: {}".format(consulta)))

def filtrar_usuarios(cpf, usuarios):
    resultado = ""
    for usuario in usuarios:
        if usuario['CPF'] == cpf:
            resultado = usuario

    if resultado != "":
        return resultado
    else:
        return None
resultado = ""

def nova_conta(agencia, numero_conta, usuarios, saldo):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!\n")
        return({"Agência": agencia, "Conta": numero_conta, "CPF": cpf, "Nome": usuario["Nome"], "Saldo": saldo, "Extrato": []})

def listar_contas():
    for conta in contas:
        linha = f"""\
        Agência: {conta["Agência"]}
        Conta: {conta["Conta"]}
        CPF: {conta["CPF"]}
        Nome: {conta["Nome"]}
        Saldo: R$ {conta["Saldo"]:.2f}
        """
        print("\n", linha)
    return()

def depositar(agencia, numero_conta, valor, contas):
    for conta in contas:
        if conta.get("Agência") == agencia and conta.get("Conta") == int(numero_conta):
            conta["Saldo"] = conta.get("Saldo") + valor
            conta["Extrato"].insert(
                len(conta["Extrato"]), 
                "{}  Depósito  R$ {:.2f}  ----  Saldo R$ {:.2f}".format(datetime.now().strftime('%d/%m/%Y %H:%M'), valor, conta["Saldo"])
                )
            return(conta)
    else:
        return(None)

def sacar(agencia, numero_conta, valor, contas):
    for conta in contas:
        if conta.get("Agência") == agencia and conta.get("Conta") == int(numero_conta) and valor < conta.get("Saldo"):
            conta["Saldo"] = conta.get("Saldo") - valor
            conta["Extrato"].insert(
                len(conta["Extrato"]), 
                "{}  Saque     R$ {:.2f}  ----  Saldo R$ {:.2f}".format(datetime.now().strftime('%d/%m/%Y %H:%M'), valor, conta["Saldo"])
                )
            return(conta)
        if conta.get("Saldo") <valor:
            return(0)
    else:
        return(None)

def extrato(agencia, numero_conta, contas):
    for conta in contas:
        if conta.get("Agência") == agencia and conta.get("Conta") == int(numero_conta):
            return(conta)
    else:
        return(None)
    
def fechar_menu():
    input("\n> Pressione qualquer tecla para voltar ao menu: ")
    system("clear")


def sair():
    #Criar função - creio não ser necessária
    return()

while opcao != 'q':
    system('clear')
    print(menu)
    opcao = menu()

    if opcao == 'd':
        system("clear")
        print("\n--- Depositar ---\n")
        agencia = input("Informe o número da agência: ")
        n_conta = int(input("Informe o número da conta: "))
        valor = float(input("Digite o valor de depósito: "))
        if valor > 0:
            conta = depositar(agencia, n_conta, valor, contas)
            if conta != None:
                print("\n*** O depósito de R$ {:.2f} foi realizado com sucesso na Agência: {} Conta: {} Beneficiário: {}. ***".format(valor, agencia, n_conta, conta["Nome"]))
            else:
                print("\n *** O depósito não foi efetuado pois, não foi encontrada a agência e a conta designada para depósito! ***")

        else: print("\n*** Valor não permitido. Só é aceito valor para depósito maior que 0. ***")
        fechar_menu()

    if opcao == 's':
        system("clear")
        print("\n--- Sacar ---\n")
        if nsaques < lim_saques:
            agenciaq = input("Informe o número da agência: ")
            n_contaq = int(input("Informe o número da conta: "))
            valorq = float(input("\nDigite o valor para saque: "))

            if valorq > 0:
                contaq = sacar(agenciaq, n_contaq, valorq, contas)
                if contaq != None and contaq != 0:
                    #system('clear')
                    print("\n*** O saque de R$ {:.2f} foi realizado com sucesso na Agência: {} Conta: {} Beneficiário: {}. ***".format(valorq, agenciaq, n_contaq, contaq["Nome"]))
                if contaq == None:
                    #system('clear')
                    print("\n *** O saque não foi efetuado pois, não foi encontrada a agência e a conta designada para depósito! ***")
                if contaq == 0:
                    print('\n*** Você não possui saldo suficiente para este saque! ***')
            if valorq > limval_saque:
                print("\n*** Valor de saque superior ao limite permitido, insira um valor menor que R$ 500,00 ***")
            if valorq < 0:
                print("\n*** Valor não permitido. Só são aceitos valores para saque maiores que 0. ***")
        else: print("\n***  quantidade de limites de saques por operação foi excedida! ***")

        fechar_menu()
        
    
    if opcao == 'e':
        system("clear")
        print("\n--- Solicitar Extrato ---\n")
        agenciae = input("\nInforme o número da agência: ")
        n_contae = int(input("\nInforme o número da conta: "))
        contae = extrato(agenciae, n_contae,contas)
        system("clear")
        print("\n--- Extrato ---\n")
        print("\nAgência: {} - Conta: {} - Beneficiário: {}\n".format(contae["Agência"], contae["Conta"], contae["Nome"]))
        for linha in contae.get("Extrato"):
            j = j + 1
            print(j, linha, '\n')
        j = 0
        print("*** Saldo em {} R$ {:.2f} ***".format(datetime.now().strftime('%d/%m/%Y %H:%M') ,contae.get("Saldo")))
        fechar_menu()
    
    if opcao == 'nu':
        system("clear")
        print("\n--- Cadastrar Novo Cliente ---\n")
        novo_usuario()
        fechar_menu()
    
    if opcao == 'nc':
        system('clear')
        print("\n--- Cadastrar Nova Conta ---\n")
        nconta = len(contas) + 1
        conta = nova_conta(agencia, nconta, usuarios, saldo)

        if conta:
            contas.append(conta)
            print("\n*** Conta criada com sucesso! ***\n")
            print("\nAgência: {} Conta: {} Proprietário: {}\n".format(conta["Agência"], conta["Conta"], conta["Nome"]))
        else:
            print("\n*** A conta não foi criada porque não foi encontrado um usuário cadastrado para o CPF. ***\n")
        fechar_menu()
        
    if opcao == 'ls':
        system("clear")
        print("\n--- Cadastrar Listar Contas Cadastradas ---\n")
        listar_contas()
        fechar_menu()

system('clear')
print("\nPrograma fechado com sucesso, muito obrigado por utilizar nossos serviços!")
print('\nTenha um bom dia!\n')
            