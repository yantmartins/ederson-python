numero = int(input("Digite um número inteiro positivo: "))
contador = 0

while numero > 0:
    numero = numero - 1
    contador = contador + 1

print(f"O número foi reduzido a zero em {contador} vezes.")
