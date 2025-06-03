def hello(nome,idade):
    print("Olá",nome, "\nSua idade é:",idade)


hello("Yan",25)    




def calcular_pagamento(qtd_horas,valor_hora):
    horas = float(qtd_horas)
    taxa = float(valor_hora)
    if horas <= 40:
        salario = horas * taxa
    else:
        h_excd = horas - 40
        salario = 40 * taxa + (h_excd*(1.5 * taxa))
    print(salario)


def soma(x,y):
    result = x + y
    return result

a = int("Primeiro número: ")
b = int("Segundo número: ")
res = soma(a,b)
print("Soma: ",res)
