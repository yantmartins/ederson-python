a = [81, 82, 83]
a.append(5) #Adiciona o parametro no final da lista
a.sort() #Ordena os numeros da lista 
a.sort(reverse=True) #Coloca a ordem reversa na lista
print(a)

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 88, 18]
print(b.index(4)) ##Busca a posição do elemento do indice passado

b.insert(1,100) #Insere o segundo parametro na posicao do primeiro parametro
print(b)
print(b.count(8)) ##Conta quantas vezes o parametro passado aparece na lista