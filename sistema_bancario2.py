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
contas = ["AGÊNCIA", "CONTA", "CPF", "NOME"]

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
    Ditige a opção: 
    """
    return(input(menu))

def novo_usuario():
    cpf = input("Informe o seu CPF: ")
    consulta = filtrar_usuarios(cpf, usuarios)
    if consulta == None:
        nome = input("Informe o nome completo: ")
        dt_nascimento = input("Informe a data de nascimento (DD/MM/AAAA): ")
        endereco = input("Informe o endereço completo (Logradouro, nº, bairro, Cidade, Estado): ")
        usuarios.append({"Nome": nome, "CPF": cpf, "Data de Nascimento": dt_nascimento, "Endereço": endereco})
        return (print("Usuaŕio cadastrado com sucesso!"))
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

def nova_conta():
    #Criar função
    return()

def listar_contas():
    #Criar função
    return()

def depositar():
    #Criar função
    return()

def sacar():
    #Criar função
    return()

def extrato():
    #Criar função
    return()

def sair():
    #Criar função
    return()

while opcao != 'q':
    print(menu)
    opcao = menu()

    if opcao == 'd': 
        valor = float(input("\nDigite o valor de depósito: "))
        if valor > 0:
            saldo = saldo + valor
            extrato.insert(i, "{}  Depósito  R$ {:.2f}".format(datetime.now().strftime('%d/%m/%Y %H:%M'), valor))
            i = i + 1
            print("\n*** Deposito de R$ {:.2f} realizado com sucesso! ***\n".format(valor))
            fechar = input("\nPressione qualquer tecla para voltar ao menu: ")
            if fechar != None: 
                system('clear')
                fechar = None
                fechar = ''

        else: print("\n*** Valor não permitido. Só é aceito valores para depósito maiores que 0. ***")
    
    if opcao == 's':
        if nsaques < lim_saques:
            valor = float(input("\nDigite o valor para saque: "))
            if valor > 0:
                if valor > limval_saque:
                    print("\n*** Valor de saque superior ao limite permitido, insira um valor menor que R$ 500,00 ***")
                else:
                    if valor >= saldo:
                        print('\n*** Você não possui saldo suficiente para este saque! ***')
                    else:
                        saldo = saldo - valor
                        extrato.insert(i, "{}  Saque     -R$ {:.2f}".format(datetime.now().strftime('%d/%m/%Y %H:%M'), valor))
                        print("\n*** O Saque de R$ {:.2f} foi realizado com sucesso! ***".format(valor))
                        nsaques = nsaques + 1
                        fechar = input("\nPressione qualquer tecla para voltar ao menu: ")
                        if fechar != None:
                            system('clear')
                            fechar = None
                            fechar = ''
            else: print("\n*** Valor não permitido. Só são aceitos valores para saque maiores que 0. ***")
        else: print("\n***  quantidade de limites de saques por operação foi excedida! ***")
    
    if opcao == 'e':
        for linha in extrato:
            j = j + 1
            print(j, linha, '\n')
        j = 0
        print("*** Saldo em {} R$ {:.2f} ***".format(datetime.now().strftime('%d/%m/%Y %H:%M') ,saldo))
        fechar = input("\nPressione qualquer tecla para voltar ao menu: ")
        if fechar != None:
            system('clear')
            fechar = None
            fechar = ''
    
    if opcao == 'nu':
        novo_usuario()

system('clear')
print("\nPrograma fechado com sucesso, muito obrigado por utilizar nossos serviços!")
print('\nTenha um bom dia!\n')
            