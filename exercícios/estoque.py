
estoque = {
    10: {'nome': 'Caderno', 'quantidade': 0},
    20: {'nome': 'Caneta', 'quantidade': 0},
    30: {'nome': 'Lápis', 'quantidade': 0},
    40: {'nome': 'Borracha', 'quantidade': 0},
    50: {'nome': 'Régua', 'quantidade': 0}
}


while True:
    print("\nEscolha a operação:")
    print("E – Entrada no estoque")
    print("S – Saída no estoque")
    print("R – Relatório")
    print("X – Sair")

    operacao = input("Digite o código da operação: ").upper()

    if operacao == 'E':
        codigo = int(input("Digite o código do produto para entrada no estoque: "))
        if codigo in estoque:
            qtd = int(input("Digite a quantidade: "))
            estoque[codigo]['quantidade'] += qtd
            print("Entrada registrada com sucesso!")
        else:
            print("Código de produto inválido.")

    elif operacao == 'S':
        codigo = int(input("Digite o código do produto para saída do estoque: "))
        if codigo in estoque:
            qtd = int(input("Digite a quantidade: "))
            if qtd <= estoque[codigo]['quantidade']:
                estoque[codigo]['quantidade'] -= qtd
                print("Saída registrada com sucesso!")
            else:
                print("Quantidade insuficiente em estoque!")
        else:
            print("Código de produto inválido.")

    elif operacao == 'R':
        print("\n--- RELATÓRIO DE ESTOQUE ---")
        for codigo in estoque:
            nome = estoque[codigo]['nome']
            qtd = estoque[codigo]['quantidade']
            print(f"{codigo} - {nome}: {qtd} unidades")
    
    elif operacao == 'X':
        print("Encerrando o programa...")
        break

    else:
        print("Operação inválida. Tente novamente.")
