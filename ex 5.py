altura= float(input("insira a sua altura ?"))
Genero= input("Escreva M para genêro masculino e F para gênero feminino ")
if Genero=='M':
	print(f"O seu peso ideial é ", (72.7 * altura) - 58)
else:
	print(f"O seu peso ideial é", (62.1 * altura) - 44.7)