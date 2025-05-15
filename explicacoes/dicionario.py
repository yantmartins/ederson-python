tradutor = {}
tradutor ["pineapple"] = "abacaxi"
tradutor ["apple"] = "maça"
tradutor ["orange"] = "laranja"
print(type(tradutor))
print(tradutor)

print("pineapple" in tradutor)


tradutor1 = {}
tradutor1 = {"pineapple":"abacaxi", "apple":"maça", "orange": "laranja"}
print(type(tradutor1))
print(tradutor1)
tradutor1.clear() ##Remove todos os elementos do dicionário
##del(tradutor1 ["apple"]) ##Deleta um elemento
print(tradutor1)


dados = {
    "Crossfox": {"km": 3500, "ano": 2005},
    "DS5": {"km": 17000, "ano": 2015},
    "Fusca": {"km": 130000, "ano": 1979},
    "Jetta": {"km": 5600, "ano": 2011},
    "Passat": {"km": 62000, "ano": 1999}  
}

print(dados)
print(dados.get("Gol","veiculo nao encontrado"))
print(dados["Fusca"]["ano"]) ##Entrega o ano do Fusca
