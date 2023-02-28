#UFCG - P1
#João Matheus Pinto Villarim Coutinho de Almeida
#Utilizando o Teorema de Herão para Calcular a Área de Triângulos

num_linhas, lista = int(input()), []
for n in range(num_linhas):
	linha = input().split()
	lista.append(linha)

lista_areas = []
for linha in lista:
	a, b, c = float(linha[0]), float(linha[1]), float(linha[2])
	sp = (a + b + c)/2
	area = (sp * (sp - a) * (sp - b) * (sp - c))**0.5
	lista_areas.append(area)

maiores, count, media = 0, 1, 0
for area in lista_areas:
	print(f"Área {count}: {area:.2f}")
	count += 1
	if area > 100:
		maiores += 1
		media += area
if maiores:
	print(f"Número maiores: {maiores}, área média: {(media/maiores):.2f}")