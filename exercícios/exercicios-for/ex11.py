preco_pao = float(input("Preço do pão: R$ "))

print("\nPanificadora Pão de Ontem - Tabela de preços")

for quantidade in range(1, 51):
    total = quantidade * preco_pao
    print(f"{quantidade} - R$ {total:.2f}")
