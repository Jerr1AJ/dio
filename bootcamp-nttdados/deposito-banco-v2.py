import time
from datetime import datetime

saldo = 0
deposito = 0
saque = float(0)
limite_saques = 10                      #Estabelecer um limite de 10 transações diárias para uma conta
numero_saques = 0
extrato = ""
data_hora_brasil = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

def menu():
    print(    
        "---===---===---===---\n"
        "      SEU BANCO   \n"
        "---===---===---===---\n"
        "Escolha uma opção:\n"
        "[1] Depositar\n"
        "[2] Sacar\n"
        "[3] Extrato\n"
        "[0] Sair\n"   
        "---===---===---===---\n"     
    )

    print('R${:.2f}'.format(saldo))

    opção = int(input('Qual opção:'))

    if opção == 1:
        depositar()
    elif opção == 2:
        sacar()
    elif opção == 3:
        ver_extrado()
    elif opção == 0:
        print("Muito obrigado por usar o SEUBANCO, até mais!")
    else:
        print("Opção inválida, digite novamente!")
        #time.sleep(3)
        menu()


def horaexec():                 #Mostre no extrato, a data e hora de todas as transações.
    # Obtendo a data e hora atuais no formato brasileiro
    data_hora_brasil = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    #print(data_hora_brasil)


def depositar():
    global saldo
    global extrato
    global data_hora_brasil

    deposito = float(input("Qual o valor do deposito: R$ "))

    if deposito > 0:
        saldo += deposito
        horaexec()
        extrato += f"{data_hora_brasil} >>>>> Deposito: R$ {deposito:.2f}\n"              #Mostrar no Extrato

    else:
        print("O valor indicado é inválido, tente novamente!")
        depositar()    

    #print('R${:.2f}'.format(saldo))
    print("Seu deposito foi confirmado!")
    #time.sleep(3)
    menu()


def sacar():
    global saldo
    global saque
    global extrato
    global numero_saques

    if numero_saques == limite_saques:
        print("Limite de saques diários alcançados! Retornando ao menu")    #Se o usuário tentar fazer uma transação após atingir o limite, deve ser informado que ele excedeu o número de transações permitidas para aquele dia.

        time.sleep(2)
        menu()

    else:
        print(
            "---===---===---===---\n"
            "Menu de Saque\n"
            "\n"
            )
        saque = float(input("Quanto você deseja sacar: R$ "))
        if saque > saldo:
            print("O valor do Saque é maior que o Saldo, tente novamente!")
            sacar()
        
        else:
            saldo -= saque
            numero_saques += 1
            extrato += f"{data_hora_brasil} >>>>> Saque nº{numero_saques}: R$ {saque:.2f}\n"
            print("Seu Saque foi confirmado!")
            #time.sleep(3)
            menu()


def ver_extrado():
    print('===---===---===\nSEU EXTRADO\n===---===---===')
    print(extrato)
    print("========")
    print(f"Saldo: R$ {saldo:.2f}")
    time.sleep(2)
    menu()

menu()






