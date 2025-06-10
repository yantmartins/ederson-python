def detectar_anagrama(palavra1, palavra2):
    palavra1 = palavra1.lower().replace(" ", "")
    palavra2 = palavra2.lower().replace(" ", "")
    return sorted(palavra1) == sorted(palavra2)


print(detectar_anagrama("casa", "saco"))
