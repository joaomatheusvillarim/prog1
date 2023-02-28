#UFCG - P1
#João Matheus Pinto Villarim Coutinho de Almeida
#Questão "números em equilíbrio", prova final

numeros, pares, impares = [], [], []

while True:
	x = int(input())
	numeros.append(x)
	if x%2==0:
		pares.append(x)
	else:
		impares.append(x)
	if len(pares)-len(impares)>2:
		text = "PARES"
		break
	elif len(impares)-len(pares)>2:
		text = "IMPARES"
		break

print(f"{text} em maior quantidade\nPARES:")
for i in pares:
	print(i)
print("IMPARES:")
for i in impares:
	print(i)