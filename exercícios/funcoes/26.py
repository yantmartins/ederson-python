def n_maiores(lista, n):
    return sorted(lista, reverse=True)[:n]

print(n_maiores([4, 1, 7, 3, 9], 3))