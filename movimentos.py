#UFCG - P1
#João Matheus Pinto Villarim Coutinho de Almeida
#Movimentos
initial, play, counter = input().split(), True, 0
initial = [int(initial[0]), int(initial[1])]
while True:
	x = input()
	if " " in x:
		x = x.split()
		x = [x[0], int(x[1])]
		counter += x[1]
	if x[0] == "B":
		initial = [initial[0] + x[1], initial[1]]
		print(f"> {initial[0]} {initial[1]}")
	elif x[0] == "C":
		initial = [initial[0] - x[1], initial[1]]
		print(f"> {initial[0]} {initial[1]}")
	elif x[0] == "D":
		initial = [initial[0], initial[1] + x[1]]
		print(f"> {initial[0]} {initial[1]}")
	elif x[0] == "E":
		initial = [initial[0], initial[1] - x[1]]
		print(f"> {initial[0]} {initial[1]}")
	else:
		break
print(counter)