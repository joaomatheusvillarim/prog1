#UFCG - P1
#João Matheus Pinto Villarim Coutinho de Almeida
#Questão "trinca", prova final

def trinca(lista):
	willbreak = False
	for i in range(len(lista)):
		for j in range(len(lista)):
			if lista[i] + 1 == lista[j]:
				for k in range(len(lista)):
					if lista[j] + 1 == lista[k]:
						if i<j:
							if j<k:
								ordem = [k, j, i]
							elif i<k:
								ordem = [j, k, i]
							else:
								ordem = [j, i, k]
						else:
							if k>i:
								ordem = [k, i, j]
							elif k>j:
								ordem = [i, k, j]
							else:
								ordem = [i, j, k]
						for item in ordem:
							lista.pop(item)
						willbreak = True
						break
			if willbreak:
				break
		if willbreak:
			break

l1 = [1, 2, 3, 5, 6, 7, 9]
l2 = [1, 7, 2, 5, 6]
trinca(l1)
trinca(l2)
print(l1)
print(l2)