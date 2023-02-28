#UFCG - P1
#João Matheus Pinto Villarim Coutinho de Almeida
#Questão "valor de venda", miniteste 8

def calcula_venda(valor, x, y, z):
	valor, x, y, z = float(valor), float(x), float(y), float(z)
	resultado = (x+y+z+1)*valor
	return resultado

while True:
	x = input().split(", ")
	if x != ["-"]:
		print(f"O valor de venda para este produto deve ser R$ {calcula_venda(*x):.2f}")
	else:
		break