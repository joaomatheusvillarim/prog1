#UFCG - P1
#João Matheus Pinto Villarim Coutinho de Almeida
#Questão "semi césar", miniteste 8

def cesar(msg, d):
	newtext = ""
	for char in msg:
		if 97 <= ord(char) <= 122:
			x = ord(char) + d
			if d > 0:
				while x > 122:
					x -= 26
			else:
				while x < 97:
					x += 26
			newtext += chr(x)
		else:
			newtext += char
	return newtext