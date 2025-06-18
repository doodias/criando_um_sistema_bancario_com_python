import os
import time

saldo = 0
limite = 500
extrato = ""
numero_saques = 1
LIMITE_SAQUES = 3

# Texto do menu principal do sistema bancário
menu = """

************
* DIO BANK *
************

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

# Texto menu de opções para depósito
deposito_menu = """ 

*********************
* DIO BANK DEPOSITO *
*********************

[1] Depositar
[2] Voltar
=>    

""" 

# Texto menu de opções para  saque
saque_menu = """ 

******************
* DIO BANK SAQUE *
******************

[1] Sacar
[2] Voltar
=>    

""" 

# Texto menu de opções para extrato
extrato_menu = """ 

********************
* DIO BANK EXTRATO *
********************

[1] Exibir Extrato
[2] Voltar
=>    

""" 

# Função para limpar o console
def clear_console(): 
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para realizar depósito
def deposito(): 
    global saldo, extrato
    try:
        clear_console()
        opcao_deposito_menu = input(deposito_menu)
        if opcao_deposito_menu == "1":
            clear_console()
            valor = float(input("Informe o valor do depósito: "))
            if valor > 0:
                saldo += float(valor)
                extrato += f"Depósito: R$ {valor:.2f}\n"
                print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
                time.sleep(2)
                clear_console()
            else:
                print("Operação falhou! O valor informado é inválido.")
        elif opcao_deposito_menu == "2":
            clear_console()
            return
        else:
            clear_console()
            print("Opção inválida. Tente novamente.")
            time.sleep(2)
            clear_console()
            return
    except ValueError:
        clear_console()
        print("Valor inválido. Por favor, insira um número válido.")
        time.sleep(2)
        clear_console()
        return

def saque(): 
    global saldo, extrato, numero_saques, LIMITE_SAQUES
    try:
        clear_console()
        opcao_saque_menu = input(saque_menu)
        if opcao_saque_menu == "1":
            clear_console()
            valor = float(input("Informe o valor do saque: "))
            if valor > 0 and numero_saques <= LIMITE_SAQUES and valor <=500 and valor <= saldo:
                saldo -= float(valor)
                extrato += f"Saque: R$ {valor:.2f}\n"
                print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
                numero_saques += 1
                time.sleep(2)
                clear_console()
            else:
                print("Operação falhou! O valor informado é inválido, saldo insulficiente ou limite de saques diários excedido.")
                time.sleep(2)
        elif opcao_saque_menu == "2":
            clear_console()
            return
        else:
            clear_console()
            print("Opção inválida. Tente novamente.")
            time.sleep(2)
            clear_console()
            return
    except ValueError:
        clear_console()
        print("Valor inválido. Por favor, insira um número válido.")
        time.sleep(2)
        clear_console()
        return

def extratobancario():
    global extrato, saldo
    clear_console()
    opcao_extrato_menu = input(extrato_menu)
    if opcao_extrato_menu == "1":
        clear_console()
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
        time.sleep(5)
        clear_console()
    elif opcao_extrato_menu == "2":
        clear_console()
        return
    else:
        clear_console()
        print("Opção inválida. Tente novamente.")
        time.sleep(2)
        clear_console()
        return

# Menu principal do sistema bancário
while True:
    clear_console()
    opcao = input(menu)
    if opcao == "d":
        deposito()
    elif opcao == "s":
        saque()
    elif opcao == "e":
        extratobancario()
    elif opcao == "q":
        print("Saindo do sistema. Até logo!")
        time.sleep(1)
        clear_console()
        break
    else:
        print("Opção inválida. Tente novamente.")
        clear_console()
        continue

    