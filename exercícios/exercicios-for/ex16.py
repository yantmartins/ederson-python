n = int(input("Digite o número de termos da sequência de Fibonacci: "))

a, b = 1, 1  # Os dois primeiros termos da sequência

print(f"Sequência de Fibonacci até o {n}-ésimo termo:")

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b  # Atualiza os valores de a e b

