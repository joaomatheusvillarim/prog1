#UFCG - P1
#João Matheus Pinto Villarim Coutinho de Almeida
#Carne de sol de Picui

recorde, tentativa = float(input()), float(input())
if recorde > tentativa:
	print("recorde mantido")
elif recorde < tentativa:
	print(f"recorde quebrado ({tentativa} kg)")
else:
	print("recorde empatado")