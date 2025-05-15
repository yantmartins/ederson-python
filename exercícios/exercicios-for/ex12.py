total_veiculos = 0
total_acidentes_cidades_pequenas = 0
quant_cidades_pequenas = 0

for i in range(5):
    print(f"\nCidade {i+1}:")
    codigo = int(input("Código da cidade: "))
    veiculos = int(input("Número de veículos de passeio: "))
    acidentes = int(input("Número de acidentes com vítimas: "))
    
    total_veiculos += veiculos

    if i == 0:
        maior_indice = acidentes
        menor_indice = acidentes
        cidade_maior = codigo
        cidade_menor = codigo
    else:
        if acidentes > maior_indice:
            maior_indice = acidentes
            cidade_maior = codigo
        if acidentes < menor_indice:
            menor_indice = acidentes
            cidade_menor = codigo

    if veiculos < 2000:
        total_acidentes_cidades_pequenas += acidentes
        quant_cidades_pequenas += 1


media_veiculos = total_veiculos / 5

if quant_cidades_pequenas > 0:
    media_acidentes_pequenas = total_acidentes_cidades_pequenas / quant_cidades_pequenas
else:
    media_acidentes_pequenas = 0


print("\nRESULTADOS:")
print(f"Maior índice de acidentes: {maior_indice} (Cidade {cidade_maior})")
print(f"Menor índice de acidentes: {menor_indice} (Cidade {cidade_menor})")
print(f"Média de veículos nas 5 cidades: {media_veiculos:.2f}")
print(f"Média de acidentes nas cidades com menos de 2000 veículos: {media_acidentes_pequenas:.2f}")
