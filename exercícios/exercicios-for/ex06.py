soma = 0

for i in range(5):
    numero = float(input(f"Digite o {i+1}º número: "))
    soma += numero


media = soma / 5

print("Soma dos números: ",soma)
print("Média dos números: ",media)
