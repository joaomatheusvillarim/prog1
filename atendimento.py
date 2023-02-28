#UFCG - P1
#João Matheus Pinto Villarim Coutinho de Almeida
#Questão "fila de atendimentos de pacientes", miniteste extra

def filas_de_atendimento(fila_unica, n):
	medicos = []
	for i in range(n):
		medicos.append([])
	for i in range(len(fila_unica)):
		for j in range(n):
			if i%n == j:
				medicos[j].append(fila_unica[i])
	return medicos

print(filas_de_atendimento(['Andre', 'Antonio', 'Bianca', 'Carlos', 'Claudia'], 3))
print(filas_de_atendimento(['Andre', 'Antonio', 'Bianca', 'Carlos'], 2))