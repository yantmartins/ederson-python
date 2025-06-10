def filtrar_maiores_que_10(lista):
    return list(filter(lambda x: x > 10, lista))

print(filtrar_maiores_que_10([4, 12, 8, 15, 3, 22]))