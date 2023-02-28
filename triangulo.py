a, b, c = int(input()), int(input()), int(input())
c1 = (a > abs(b - c)) and (b+c > a)
c2 = (b > abs(a - c)) and (a+c > b)
c3 = (c > abs(a - b)) and (a+b > c)
if c1 and c2 and c3:
	print("triangulo valido. {}".format(a+b+c))
else:
	print("triangulo invalido.")