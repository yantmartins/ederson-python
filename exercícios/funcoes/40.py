def juros_compostos(capital, taxa, tempo):
    return capital * (1 + taxa) ** tempo

print(juros_compostos(1000, 0.05, 12))