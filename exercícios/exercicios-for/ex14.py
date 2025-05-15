print("Digite -999 para encerrar.")

soma = 0
cont = 0

while True:
    temp = float(input("Temperatura: "))
    if temp == -999:
        break
    mes = input("Mês: ")
    ano = input("Ano: ")

    if cont == 0:
        maior = menor = temp
        mes_maior = mes_menor = mes
        ano_maior = ano_menor = ano
    else:
        if temp > maior:
            maior = temp
            mes_maior = mes
            ano_maior = ano
        if temp < menor:
            menor = temp
            mes_menor = mes
            ano_menor = ano

    soma += temp
    cont += 1

if cont > 0:
    print(f"\nMaior: {maior}°C em {mes_maior}/{ano_maior}")
    print(f"Menor: {menor}°C em {mes_menor}/{ano_menor}")
    print(f"Média: {soma / cont:.2f}°C")
else:
    print("Nenhuma temperatura registrada.")
