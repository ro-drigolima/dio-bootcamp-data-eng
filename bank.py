menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

depositos = []  # para salvar a lista de depósitos
saques = []     # para salvar a lista de saques

while True:
    opcao = input(menu)

    if opcao == "d":
        print("\n============ DEPÓSITO ============\n")
        
        valor_depositado = int(input("Digite o valor a ser depositado: "))
        
        if valor_depositado >= 0:
            depositos.append(valor_depositado)
            saldo += valor_depositado
        else:
            print("O valor depositado precisa ser um inteiro positivo.")
    
    elif opcao == "s":
        print("\n============ SAQUE ============\n")

        if numero_saques < LIMITE_SAQUES:
            valor_a_sacar = int(input("Digite o valor a ser sacado: \n=> "))
            
            if valor_a_sacar > limite:
                print("O limite por saque é R$ 500,00. Tente novamente.")
            elif valor_a_sacar <= saldo:
                saques.append(valor_a_sacar)
                saldo -= valor_a_sacar
                numero_saques += 1
            else:
                print("Saldo insuficiente para saque.")
        else:
            print("Você excedeu o limite de 3 saques por dia. Tente outro dia.")

    elif opcao == "e":
        print("\n============ EXTRATO ============\n")

        # Listando os depósitos
        print("===== DEPÓSITOS:\n")
        if len(depositos) > 0:
            for i in range(len(depositos)):
                print(f"{i+1}° depósito: R$ {depositos[i]:.2f}")
        else:
            print("Nenhum depósito realizado.")

        # Listando os saques
        print("\n===== SAQUES:\n\n")
        if len(saques) > 0:
            for i in range(len(saques)):
                print(f"{i+1}° saque: R$ {saques[i]:.2f}")
        else:
            print("Nenhum saque realizado.")
        
        # Exibindo saldo
        print(f"\nSaldo: R$ {saldo:.2f}\n")

    elif opcao == "q":
        print("Saindo...\n")
        break

    else:
        print("Operação inválida. Tente novamente.")
