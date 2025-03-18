nome = input("Informe o seu nome: ")
cpf = input("Informe o seu CPF: ")
rg = input("Informe o seu RG: ")
data_nasc = input("Informe a sua data de nascimento (DD/MM/AAAA): ")
sexo = input("Informe o seu sexo: ")
peso = input("Informe o seu peso: ")
sangue = input("Informe o seu tipo sanguíneo: ")
renda = input("Informe a sua renda: ")
endereco = input("Informe o seu endereço: ")
telefone = input("Informe o seu telefone: ")
cidade = input("Informe a sua cidade: ")
estado = input("Informe o estado que você mora: ")

relatorio = f"""
=============================
        RELATÓRIO PESSOAL
=============================
Nome: {nome}
CPF: {cpf}
RG: {rg}
Data de Nascimento: {data_nasc}
Sexo: {sexo}
Peso: {peso} kg
Tipo Sanguíneo: {sangue}
Renda: R$ {renda}
Endereço: {endereco}
Telefone: {telefone}
Cidade: {cidade}
Estado: {estado}
=============================
"""
print(relatorio)