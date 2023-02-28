x, lista = int(input()), []
for i in range(x):
	lista.append(int(input()))
print("---")
a, b = int(input()), int(input())
x, y, z = 0, 0, 0
for i in lista:
	if i<a:
		x += 1
	elif i>a:
		if i<b:
			y += 1
		elif i>b:
			z += 1
print(f"{x} antes\n{y} entre\n{z} depois")