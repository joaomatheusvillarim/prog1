lista = []
while True:
	x = input()
	lista.append(x)
	c, v = 0, 0
	for i in x:
		if i in "aeiouAEIOU":
			v += 1
		else:
			c += 1
	if c > v:
		print(len(lista))
		break