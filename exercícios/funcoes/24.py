def substituir_vogais(s):
    vogais = "aeiouAEIOU"
    return ''.join("*" if c in vogais else c for c in s)

print(substituir_vogais("Python é divertido"))