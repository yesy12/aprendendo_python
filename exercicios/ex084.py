pessoas =  []
dados = []
menorPeso = []
maiorPeso = []

while True:
	dados.append(input("Digite o nome da pessoa: ").strip())
	dados.append(int(input("Digite o peso da pessoa: ").strip()))
	
	pessoas.append(dados[:]) 
	
	dados = []
	
	cont = input("Deseja continuar [s/n]? ").strip().upper()
	if(cont == "N"):
		break


for pos,pessoa in enumerate(pessoas):
	if(pos == 0):
		menorPeso.append(pessoa)
		maiorPeso.append(pessoa)
	else:
		if(pessoa[1] == menorPeso[0][1]):
			menorPeso.append(pessoa)
		elif(pessoa[1] < menorPeso[0][1]):
			menorPeso = []
			menorPeso.append(pessoa)
			
		if(pessoa[1] == maiorPeso[0][1]):
			maiorPeso.append(pessoa)
		elif(pessoa[1] > maiorPeso[0][1]):
			maiorPeso = []
			maiorPeso.append(pessoa)
			
print(f"Foram adicionadas {len(pessoas)} pessoas")
print(f"O menor peso foi {menorPeso[0][1]}kgs das pessoas",end="")
for pessoa in menorPeso:
	print(f" {pessoa[0]} ",end="")
	
print(f"\nO maior peso foi {maiorPeso[0][1]}kgs das pessoas",end="")
for pessoa in maiorPeso:
	print(f" {pessoa[0]} ",end="")
print("\n")