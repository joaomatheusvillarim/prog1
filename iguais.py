#UFCG - P1
#João Matheus Pinto Villarim Coutinho de Almeida
#Questão "identifica iguais", prova final

l1, l2, l3 = input().split(), input().split(), []

if len(l1) > len(l2):
	x = len(l2)
else:
	x = len(l1)

for i in range(x):
	if l1[i] == l2[i]:
		l3.append([int(l1[i]), i+1])

for item in l3:
	print(f"{item[1]}: {item[0]}")