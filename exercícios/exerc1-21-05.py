clientes = []
passagens = []
avioes = []
tripulacao = []

while True:
    print("\n=== MENU ===")
    print("1 - Cadastrar Cliente")
    print("2 - Cadastrar Passagem")
    print("3 - Cadastrar Avião")
    print("4 - Cadastrar Tripulação")
    print("5 - Ver Relatórios")
    print("6 - Sair")
    
    opcao = input("Opção: ")

    if opcao == "1":
        try:
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            clientes.append([nome, idade])
            print("Cliente cadastrado!\n")
        except:
            print("Erro: idade deve ser número.\n")

    elif opcao == "2":
        try:
            origem = input("Origem: ")
            destino = input("Destino: ")
            valor = float(input("Valor: "))
            desconto = valor * 0.05
            passagens.append([origem, destino, valor, desconto])
            print("Passagem cadastrada!\n")
        except:
            print("Erro: valor deve ser número.\n")

    elif opcao == "3":
        try:
            modelo = input("Modelo: ")
            capacidade = int(input("Capacidade: "))
            avioes.append([modelo, capacidade])
            print("Avião cadastrado!\n")
        except:
            print("Erro: capacidade deve ser número.\n")

    elif opcao == "4":
        try:
            nome = input("Nome: ")
            cargo = input("Cargo: ")
            tripulacao.append([nome, cargo])
            print("Tripulante cadastrado!\n")
        except:
            print("Erro no cadastro.\n")

    elif opcao == "5":
        print("\n--- RELATÓRIOS ---")
        print("Clientes:", clientes)
        print("Passagens:", passagens)
        print("Aviões:", avioes)
        print("Tripulação:", tripulacao)

    elif opcao == "6":
        print("Saindo...")
        break

    else:
        print("Opção inválida.\n")
