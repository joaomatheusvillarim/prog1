#UFCG - P1
#João Matheus Pinto Villarim Coutinho de Almeida
#Comissão

nome = input("Qual é o nome do(a) vendedor(a)? ")
valor = float(input("Qual é o valor da venda? "))
if valor <= 500:
	comissao = valor * 0.05
else:
	comissao = valor * 0.1
	nome = nome[0:5]
print(f"O valor da comissão para o(a) vendedor(a) {nome} é R$ {comissao:.2f}.")