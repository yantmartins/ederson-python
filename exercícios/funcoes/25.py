def elementos_unicos(lista):
    unicos = []
    for item in lista:
        if item not in unicos:
            unicos.append(item)
    return unicos

print(elementos_unicos([1, 2, 2, 3, 1, 4]))