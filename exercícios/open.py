
nomes = []
idades = []
sexos = []
cpfs = []
enderecos = []
cidades = []
estados = []

opcao = ""

print("\n---- SISTEMA DE CADASTRO ----")

while opcao != "3":
    print("\n1 - Cadastrar pessoa")
    print("2 - Consultar dados")
    print("3 - Sair e salvar")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        continuar = "S"
        while continuar == "S":
            try:
                nome = input("Nome: ")
                idade = int(input("Idade: "))
                sexo = input("Sexo (M/F): ").upper()
                if sexo != "M" and sexo != "F":
                    raise ValueError("Sexo inválido. Use M ou F.")
                cpf = input("CPF (somente números): ")
                endereco = input("Endereço: ")
                cidade = input("Cidade: ")
                estado = input("Estado (sigla): ").upper()

                nomes.append(nome)
                idades.append(idade)
                sexos.append(sexo)
                cpfs.append(cpf)
                enderecos.append(endereco)
                cidades.append(cidade)
                estados.append(estado)

                print("Cadastro realizado com sucesso.")
                continuar = input("Deseja cadastrar outra pessoa? (S/N): ").upper()
            except ValueError as erro:
                print("Erro no cadastro:", erro)
                continuar = input("Deseja tentar novamente? (S/N): ").upper()

    elif opcao == "2":
        if len(nomes) == 0:
            print("Nenhum dado cadastrado.")
        else:
            print("\nCampos disponíveis para consulta: nome, idade, sexo, cpf, endereco, cidade, estado")
            campo = input("Digite o campo que deseja consultar: ")

            if campo == "nome":
                for item in nomes:
                    print(item)
            elif campo == "idade":
                for item in idades:
                    print(item)
            elif campo == "sexo":
                for item in sexos:
                    print(item)
            elif campo == "cpf":
                for item in cpfs:
                    print(item)
            elif campo == "endereco":
                for item in enderecos:
                    print(item)
            elif campo == "cidade":
                for item in cidades:
                    print(item)
            elif campo == "estado":
                for item in estados:
                    print(item)
            else:
                print("Campo inválido.")

    elif opcao == "3":
        with open("cadastro.txt", "w", encoding="utf-8") as arquivo:
            for i in range(len(nomes)):
                linha = "Nome: " + nomes[i] + ", Idade: " + str(idades[i]) + ", Sexo:" + sexos[i] + ", Endereço: " + enderecos[i] + ", Cidade: " + cidades[i] + ", Estado: " + estados[i]
                arquivo.write(linha + "\n")
                arquivo.write("-" * 100 + "\n")
        print("Dados salvos no arquivo 'cadastro.txt'. Programa encerrado.")
    else:
        print("Opção inválida. Escolha 1, 2 ou 3.")
