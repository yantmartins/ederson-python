clientes = []

while True:
    print("\n=== Cadastro de Cliente ===")
    nome = input("Nome completo: ")
    cpf = input("CPF: ")
    rg = input("RG: ")
    telefone = input("Telefone: ")
    agencia = input("Número da agência: ")
    conta = input("Número da conta: ")
    
    while True:
        try:
            saldo = float(input("Saldo inicial (R$): "))
            break
        except ValueError:
            print("Digite um valor válido para o saldo.")

    cliente = [nome, cpf, rg, telefone, agencia, conta, saldo]
    clientes.append(cliente)

    print("\n--- Cliente cadastrado com sucesso! ---")
    print(f"Nome: {cliente[0]}")
    print(f"CPF: {cliente[1]}")
    print(f"RG: {cliente[2]}")
    print(f"Telefone: {cliente[3]}")
    print(f"Agência: {cliente[4]}")
    print(f"Conta: {cliente[5]}")
    print(f"Saldo: R$ {cliente[6]:.2f}")

    while True:
        print("\n=== Menu Bancário ===")
        print("1 - Ver Saldo")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            print(f"Saldo atual: R$ {cliente[6]:.2f}")

        elif opcao == '2':
            try:
                valor = float(input("Valor para depósito: R$ "))
                if valor > 0:
                    cliente[6] += valor
                    print(f"Depósito realizado. Novo saldo: R$ {cliente[6]:.2f}")
                else:
                    print("O valor deve ser positivo.")
            except ValueError:
                print("Digite um valor numérico.")

        elif opcao == '3':
            try:
                valor = float(input("Valor para saque: R$ "))
                if valor > 0:
                    if valor <= cliente[6]:
                        cliente[6] -= valor
                        print(f"Saque realizado. Novo saldo: R$ {cliente[6]:.2f}")
                    else:
                        print("Saldo insuficiente.")
                else:
                    print("O valor deve ser positivo.")
            except ValueError:
                print("Digite um valor numérico.")

        elif opcao == '4':
            print("Encerrando sessão do cliente atual...\n")
            break

        else:
            print("Opção inválida. Tente novamente.")
