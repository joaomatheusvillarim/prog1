x, a = input().split(), 0
for i in range(1, len(x)):
	if x[i] == x[i-1]:
		a += 1
print(a)