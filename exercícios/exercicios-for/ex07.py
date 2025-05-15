n = int(input("Quantos números você vai digitar? "))

soma = 0

for i in range(n):
    numero = float(input(f"Digite o {i+1}º número: "))
    
    if i == 0:
        menor = numero
        maior = numero
    else:
        if numero < menor:
            menor = numero
        if numero > maior:
            maior = numero

    soma += numero

print("Menor valor:", menor)
print("Maior valor:", maior)
print("Soma dos valores:", soma)
