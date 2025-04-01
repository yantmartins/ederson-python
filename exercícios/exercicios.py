#Exercicio 1
lista = [1,2,3,4,5]
print(lista)
print(max(lista))
print(min(lista))
print(len(lista))
print(sum(lista))

#Exercicio 2
lista2 = [1,2,1,5,6,4,3,1]
print(lista2.count(1))

#Exercicio 3
frutas = ['Banana','Uva','Pera','Kiwi','Morango']
frutas[1] = 'Laranja' #Substitui o segundo elemento na lista
print(frutas)

#Exercicio 4
t = [[1,2],[3],[4,5,6]]

print(sum(sum(t, [])))
               
#Exercicio 6
y = [1,2,3,4]
y.pop(-1)
y.pop(0)
print(y)

#Exercicio 7
country = ["Alemanha", "Itália", "Japão"]
country.append("Brasil")
print(country)
country.extend(["Canadá","Estados Unidos","México"])
print(country)
country.extend(["Argentina","Bolívia","Chile","Colômbia","Equador","Guiana","Paraguai","Peru","Suriname","Uruguai","Venezuela"])
print(country)
country.extend(["Belize","Costa Rica","El Salvador","Guatemala","Honduras","Nicarágua","Panamá"])
print(country)
country.extend(["Ottawa","Washington","Mexico City","Belmopan","San Jose","San Salvador","Guatemala City","Tegucigalpa","Manágua","Panama City","Buenos Aires","Sucre","Brasília","Santiago","Bogotá","Quito","Georgetown","Assunção","Lima","Paramaribo","Montevideo","Caracas"])
print(country)