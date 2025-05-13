
n = int(input("Total de eleitores: "))


v1 = v2 = v3 = 0

for i in range(n):
    voto = int(input(f"Eleitor {i+1}, vote (1, 2 ou 3): "))
    if voto == 1:
        v1 += 1
    elif voto == 2:
        v2 += 1
    elif voto == 3:
        v3 += 1


print(f"\nCandidato 1: {v1} votos")
print(f"Candidato 2: {v2} votos")
print(f"Candidato 3: {v3} votos")


if v1 > v2 and v1 > v3:
    print("Candidato 1 é o campeão!")
elif v2 > v1 and v2 > v3:
    print("Candidato 2 é o campeão!")
elif v3 > v1 and v3 > v2:
    print("Candidato 3 é o campeão!")
else:
    print("Houve empate!")
