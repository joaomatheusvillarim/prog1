x = int(input())
y = (x%400==0) or ((x%4==0) and (x%100!=0))
if y:
	print(x, "é bissexto")
else:
	print(x, "não é bissexto")