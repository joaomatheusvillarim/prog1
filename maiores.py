#UFCG - P1
#João Matheus Pinto Villarim Coutinho de Almeida
#Questão "remove maiores", miniteste extra

def ordenar(lista):
	newlista = []
	while lista:
		minimo = lista[0]
		for item in lista:
			if item < minimo:
				minimo = item
		newlista.append(minimo)
		lista = list(set(lista).difference([minimo]))
	return newlista

def remove_maiores(lista):
	maior = ordenar(list(set(lista)))[-1]
	lista2 = []
	for item in lista:
		if item != maior:
			lista2.append(item)
	return lista2

print(remove_maiores([8, 7, 3, 8, 2]))