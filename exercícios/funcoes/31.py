def calculadora(n1, n2, operacao):
    if operacao == '+':
        return n1 + n2
    elif operacao == '-':
        return n1 - n2
    elif operacao == '*':
        return n1 * n2
    elif operacao == '/':
        return n1 / n2 if n2 != 0 else "Erro: divisão por zero"
    else:
        return "Operação inválida"

print(calculadora(10, 5, '*'))