while True:
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a sua senha: ")

    if senha == usuario:
        print("ERRO! A senha não pode ser igual ao nome de usuário. Tente novamente \n")
    else:
        break

print("Cadastro realizado com sucesso!")        