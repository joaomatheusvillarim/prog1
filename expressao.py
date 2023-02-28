#UFCG - P1
#João Matheus Pinto Villarim Coutinho de Almeida
#Expressao ABCD

a, b, c, d = input(), input(), input(), input()
dc, ca, bb, aad = int(f"{d}{c}"), int(f"{c}{a}"), int(f"{b}{b}"), int(f"{a}{a}{d}")
expressao = dc - int(a) - int(b) - ca - int(d) + bb + aad
print(expressao)