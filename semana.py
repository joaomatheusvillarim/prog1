#UFCG - P1
#João Matheus Pinto Villarim Coutinho de Almeida
#Qual o dia da semana?

dias = ["domingo", "segunda", "terca", "quarta", "quinta", "sexta", "sabado"]
dia1, diax = input(), int(input())
for x in range(0, 7):
	if dias[x] == dia1:
		resto = x
diax = diax%7
print(dias[(diax+resto-1)%7])