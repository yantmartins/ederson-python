print("-- Reservatório de Água --") 

altura = float(input("Digite a altura (cm): ")) 
largura = float(input("Digite a largura (cm): ")) #Faltava um parenteses e estava como INT
comprimento = float(input("Digite o comprimento (cm): ")) #Faltava sinal de = 
c_diario = float(input("Digite o valor do consumo médio diário (litros/dia): "))

cap_total = (altura * largura * comprimento) / 1000 # Comentario com as aspas triplas
auton_reser = cap_total / c_diario

print(f"\nCapacidade do Reservatório: {cap_total:.2f} litros") #melhor formatacao de saida
print(f"Autonomia do Reservatório: {auton_reser:.2f} dias")

if auton_reser < 2:
    print("Consumo Elevado") #identacao corrigida 
elif 2 <= auton_reser <= 7:
    print("Consumo Moderado")
else:
    print("Consumo Baixo")
