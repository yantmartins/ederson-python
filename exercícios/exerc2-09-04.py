
sexo = input("Digite a letra do sexo (F para Feminino, M para Masculino, O para Outros): ").upper()

if sexo == 'F':
    print("Feminino")
else:
    if sexo == 'M':
        print("Masculino")
    else:
        if sexo == 'O':
            print("Outros")
        else:
            print("Sexo Inválido")
