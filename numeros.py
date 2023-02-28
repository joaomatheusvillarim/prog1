#UFCG - P1
#João Matheus Pinto Villarim Coutinho de Almeida
#Números iguais

a, b, c = int(input()), int(input()), int(input())
lista = [a, b, c]
count1 = 0
for x in lista:
	count2 = -1
	for y in lista:
		if x==y:
			count2+=1
	if count2:
		count1+=1
print(count1)