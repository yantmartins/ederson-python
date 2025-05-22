
estoque = {
    "arroz": 10,
    "feijão": 5,
    "macarrão": 8,
    "leite": 12
}


produto = input("Digite o nome do produto que você deseja procurar: ")


if produto in estoque:
    print(f"Temos {estoque[produto]} unidades de {produto} em estoque.")
else:
    print(f"Desculpe, o produto '{produto}' não está disponível no estoque.")
