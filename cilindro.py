print("Cálculo da Superfície de um Cilindro\n---")
d = float(input("Medida do diâmetro? "))
h = float(input("Medida da altura? "))
area = 2 * 3.1415 * ((d/2)**2) + h * d * 3.1415
print(f"---\nÁrea calculada: {area:.2f}")