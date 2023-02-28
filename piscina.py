#UFCG - P1
#João Matheus Pinto Villarim Coutinho de Almeida
#Volume da piscina

comprimento, largura, profundidade = float(input()), float(input()), float(input())
volume = comprimento*largura*profundidade*1000
print(f"A piscina comporta {volume:.2f} litros de água.")