#UFCG - P1
#João Matheus Pinto Villarim Coutinho de Almeida
#Numeros oscilantes

numero = input()
i = int(numero[0])%2
valido = True
for x in range(0, len(numero)):
	if x%2==0:
		if int(numero[x])%2 != i:
			valido = False
	else:
		if int(numero[x])%2 == i:
			valido = False
if valido:
	print(f"verdadeiro: {len(numero)} algarismos.")
else:
	print(f"falso: {len(numero)} algarismos.")