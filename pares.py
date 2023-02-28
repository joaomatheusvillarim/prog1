x, lista, pares, counter1, counter2 = int(input()), [], 0, 0, 0
for i in range(x):
	nmr = int(input())
	if nmr%2==0:
		pares += nmr
		counter1 += 1
	lista.append(nmr)
for i in lista:
	if i>(pares/counter1):
		counter2 += 1
print(f"média dos pares: {pares/counter1}\nacima da média: {counter2}")