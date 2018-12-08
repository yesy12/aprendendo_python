matrizLista = []
linhas = []
print("Matriz 3x3")
for matriz in range(0,3):
	for numero in range(0,3):
		num = int(input(f"digite um numero para [{matriz}/{numero}]: ").strip())
		linhas.append(num)
	matrizLista.append(linhas[:])
	linhas = []
		
for pos,linha in enumerate(matrizLista):
	for numeros in matrizLista[pos]:
		print(f"[ {numeros} ]",end="")
	print("")