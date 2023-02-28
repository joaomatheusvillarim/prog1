run = True
while run:
	n1, n2, n3 = input("nome 1? "), input("nome 2? "), input("nome 3? ")
	ordem = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	for i in range(26):
		if n1.startswith(ordem[i]):
			for j in range(i, 26):
				if n2.startswith(ordem[j]):
					for k in range(j, 26):
						if n3.startswith(ordem[k]):
							print(n1, n2, "de", n3)
							global willbreak
							willbreak = True
							break
					else:
						print("nomes inválidos: tente novamente")
				if willbreak:
					break
			else:
				print("nomes inválidos: tente novamente")