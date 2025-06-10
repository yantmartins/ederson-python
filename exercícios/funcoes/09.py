def nomes_maiores_que_5(nomes):
    return [nome for nome in nomes if len(nome) > 5]

lista_nomes = ["Ana", "Eduardo", "Carlos", "João", "Beatriz"]
print("Nomes com mais de 5 letras:", nomes_maiores_que_5(lista_nomes))
