while True:
    nota = float(input("Digite uma nota entre 0 e 10: "))
    if 0 <= nota <= 10:
        break
    print("Valor inválido! A nota deve estar entre 0 e 10")

print(f"Nota registrada: {nota}")