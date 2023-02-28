valores = []
for x in range(3):
	valores.append(float(input()))
for x in valores:
	print("{:.2f}".format(x/4000))
print("{:.2f}".format(sum(valores)/12000))