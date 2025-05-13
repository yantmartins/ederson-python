
n = int(input("Digite o número de pessoas: "))


soma_idades = 0


for i in range(n):
    idade = int(input(f"Digite a idade da pessoa {i + 1}: "))
    soma_idades += idade


media = soma_idades / n

print(f"Média das idades: {media:.2f}")

if media >= 0 and media <= 25:
    print("A turma é jovem.")
elif media <= 60:
    print("A turma é adulta.")
else:
    print("A turma é idosa.")
