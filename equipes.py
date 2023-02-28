#UFCG - P1
#João Matheus Pinto Villarim Coutinho de Almeida
#Equipes
lista = []
while True:
	x = input()
	if x == "-":
		break
	else:
		lista.append(x)
if len(lista) == 4:
	a = "Modalidade -> Handebol"
elif len(lista) == 5:
	a = "Modalidade -> Basquete"
elif len(lista) == 6:
	a = "Modalidade -> Volei"
elif len(lista) == 11:
	a = "Modalidade -> Futebol"
print(a)