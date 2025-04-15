valor_hora = float(input("Informe o valor da sua hora de trabalho: R$ "))
horas_trabalhadas = float(input("Informe a quantidade de horas trabalhadas no mês: "))

salario_bruto = valor_hora * horas_trabalhadas

if salario_bruto <= 900:
    imposto_renda = 0
elif salario_bruto <= 1500:
    imposto_renda = 5
elif salario_bruto <= 2500:
    imposto_renda = 10
else:
    imposto_renda = 20

imposto_renda = (imposto_renda / 100) * salario_bruto
inss = 0.10 * salario_bruto                
fgts = 0.11 * salario_bruto
total_descontos = imposto_renda + inss
salario_liquido = salario_bruto - total_descontos

print("\nTabela")
print(f"Salário Bruto: ({valor_hora} * {horas_trabalhadas})     : R${salario_bruto:.2f}")
print(f"(-) Imposto de Renda ({imposto_renda}%)     : R${imposto_renda:.2f}")
print(f"(-) INSS (10%)    : R${inss:.2f}")
print(f"FGTS (11%)        : R${fgts:.2f}")
print(f"Total de descontos: R${total_descontos:.2f}")
print(f"Salário Líquido   : R${salario_liquido:.2f}")