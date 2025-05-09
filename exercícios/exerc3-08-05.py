num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

soma = 0  

if num1 < num2:
    for i in range(num1 + 1, num2):
        print(i)
        soma += i

elif num2 < num1:
    for i in range(num2 + 1, num1):
        print(i)
        soma += i

else:
    print("Não há números no intervalo (valores iguais).")


if num1 != num2:
    print("Soma dos números:", soma)
