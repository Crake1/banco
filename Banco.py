menu = """

[1] Sacar
[2] Depositar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

while True:

    opcao = input(menu)

    if opcao == "2":
        valor = float(input("Qual valor gostaria de depositar ? "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposíto: R$ {valor:.2f}\n"
        	
        else:
            print("Valor informado é invalido ! ")
        

    
    elif opcao == "1":
        valor = float(input("Qual valor deseja sacar ? "))

        excedeu_saldo = valor > saldo 

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >=  LIMITE_SAQUE 

        if excedeu_saldo:
            print("Operação falhou. Você não tem saldo suficiente !")
        
        elif excedeu_limite:
            print("Operação falhou. Você excedeu o valor limite de saque!")

        elif excedeu_limite:
            print("Operação falhou. Você excedeu o Limite de 3 saques !")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2}\n"
            numero_saques += 1

        else:
            print("Opreção falhou. Valor informado é invalido ! ")

       
    
    elif opcao == "3":
        print("\n===============Extrato===============")
        print(" Não foram realizadas movimentações" if not extrato else extrato)
        print(f"\n Saldo; R$ {saldo:.2f}")
        print("======================================")

    elif opcao == "0":
        break

    else:
        print("Opção nao encontrada !!")