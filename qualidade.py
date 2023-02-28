a, b = float(input()), float(input())
ratio = (1 - b/a) * 100
if ratio < 5:
	q = "Produto qualis A."
elif ratio < 10:
	q = "Produto em conformidade."
else:
	q = "Produto não conforme."
print(f"{ratio:.1f}% do peso do produto é de água congelada.\n{q}")