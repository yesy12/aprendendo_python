matrizLista = []
linhas = []
pares = 0
soma3coluna = 0
maiorValor = 0
print("Matriz 3x3")
for matriz in range(1,4):
	for numero in range(1,4):
		num = int(input(f"digite um numero para [{matriz}:{numero}]: ").strip())
		linhas.append(num)
	matrizLista.append(linhas[:])
	linhas = []
		
for pos in range(0,len(matrizLista)):
	for posicao,numeros in enumerate(matrizLista[pos]):
		print(f"[ {numeros:^5} ]",end="")
		if(numeros % 2 == 0):
			pares += numeros
		if(posicao == 2):
			soma3coluna += numeros
		if(pos == 1):
			maiorValor = max(matrizLista[pos])
	print("")
	
print(f"A soma de todos os pares foram {pares}")
print(f"A soma da 3° coluna é {soma3coluna}")
print(f"O maior Valor é {maiorValor}")