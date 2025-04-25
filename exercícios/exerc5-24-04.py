while True:
    nome = input("Digite seu nome: ")
    if len(nome) >= 3:
        break
    print("ERRO! O nome deve ter mais de 3 caracteres.")

while True:
    idade = int(input("Digite sua idade: "))
    if 0 <= idade <= 150:
        break
    print("ERRO! A idade deve estar entre 0 e 150.")

while True:
    salario = float(input("Digite seu salário: "))
    if salario > 0:
        break
    print("ERRO! O salário deve ser maior que zero.") 

while True:
    sexo = input("Digite seu sexo (f - feminino, m - masculino, o - outro): ").lower()
    if sexo == "f" or sexo == "m" or sexo == "o":
        break
    print("ERRO! O sexo deve ser 'f', 'm' ou 'o'.")

while True:
    estado_civil = input("Digite seu estado civil (s - solteiro, c - casado, v - viúvo, d - divorciado): ").lower()
    if estado_civil in ["s", "c", "v", "d"]:
        break
    print("ERRO! O estado civil deve ser 's', 'c', 'v', ou 'd'.")

print("\nInformações registradas com sucesso!")        
