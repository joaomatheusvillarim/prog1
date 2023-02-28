x, counter = input(), 0
newstring = x[0]
for i in range(1, len(x)):
	if x[i] in "aA":
		newstring, counter = newstring + "4", counter + 1
	elif x[i] in "eE":
		newstring, counter = newstring + "3", counter + 1
	elif x[i] in "iI":
		newstring, counter = newstring + "1", counter + 1
	elif x[i] in "oO":
		newstring, counter = newstring + "0", counter + 1
	else:
		newstring = newstring + x[i]
print(f"{newstring} ({counter} troca(s))")