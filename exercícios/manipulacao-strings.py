##MANIPULAÇAO DE STRINGS
a = "Yan Torres"
b = '12345'
print(len(a)) #Imprime o número de caracteres
print(a.capitalize()) #Deixa a primeira letra maiscula
print(a.upper()) #Torna tudo maiusculo
print(a.lower()) ##Torna tudo minusculo
print(a.islower()) ##Verifica se tudo o que é digitado é minusculo e retorna True ou False
print(a.isupper()) ##Verifica se tudo o que é digitado é maiusculo e retorna True ou False
print(b.isdigit()) ###Verifica se a string possui APENAS números inteiros e retorna True ou False
print(a.replace("Torres","Martins"))

c = "Yan-Torres-Martins"
print(c.split("-")) #Metodo Split separa uma string usando sep como separador, retorna uma lista das substrings
print(c.find("Martins")) #O método FIND retorna o indice onde a substring começa
print("Torres" in c) ##Verifica se a substring é parte de outra string, retorna True ou False
print(c.count("a")) #Retorna a frequencia de ocorrencia do parametro passado, no caso ali da letra A

s = "Olá, mundo!"
print(s[0]) #Printa no indice passado como parametro
print(s[2]) #Printa no indice passado como parametro
print(s[6]) #Printa no indice passado como parametro
print(s[-1])
print(s[-9])
print(s[-5])
print(s[1:3]) #Printa do 1 ao 2, o 3 é o limite passado como parametro mas nao entra no print


