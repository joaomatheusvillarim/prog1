lista = []
while True:
	x = input()
	if x == "-":
		break
	else:
		lista.append(x)
counter, reprovados = 0, 0
while counter < len(lista):
	counter2, faltas = 0, 0
	while counter2 < 14:
		if lista[counter][counter2] == "f":
			faltas += 1
		counter2 += 1
	if faltas >= 8:
		reprovados += 1
	counter += 1
print(f"{reprovados} aluno(s) reprovado(s) por falta.")