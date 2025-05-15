print("Lojas Quase Dois - Tabela de preços")

for quantidade in range(1, 51):
    valor = quantidade * 1.99
    print(f"{quantidade} - R$ {valor:.2f}")
