print("Cálculo da Superfície de um Cilindro\n---")
diametro, altura, pi = float(input("Medida do diâmetro? ")), float(input("Medida da altura? ")), 3.1415
area = (pi * diametro**2)/2 + altura*diametro*pi
print("---\nÁrea calculada: {:.2f}".format(area))                                                                                                                                              