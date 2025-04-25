
opcao = ""

while opcao!= "X" and opcao != "x":
    print("\n==== CALCULADORA ====")
    print("A - Adição")
    print("S - Subtração")
    print("M - Multiplicação")
    print("D - Divisão")
    print("X - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "A" or opcao == "a":
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        resultado = a + b
        print(f"Resultado da adição é de: {resultado}")

    elif opcao == "S" or opcao == "s":
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        resultado = a - b
        print(f"Resultado da subtração é de: {resultado}")

    elif opcao == "M" or opcao == "m":
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: ")) 
        resultado = a * b
        print(f"Resultado da multiplicação é de: {resultado}")

    elif opcao == "D" or opcao == "d":
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        if b != 0:
            resultado = a / b
            print(f"Resultado da divisão é de: {resultado}")
        else:
            print("Não é possível dividir por 0") 

    elif opcao == "X" or opcao == "x":
        print("Calculadora encerrada")

    else:
        print("Opçao inválida")                         