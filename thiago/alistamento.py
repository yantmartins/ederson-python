nome = input("Digite seu nome: ")
genero = input("Digite seu genero M para masculino F para feminino: ")
idade = int(input("Digite sua idade: "))

if idade >= 17:
    print("Maior ou igual a 17")
    if genero == "M":
        print("Obrigatorio o alistamento militar")
    else:
        print("Nao é obrigatório se alistar")

else:
    print("Calma jovem gafanhoto!")        
